import discord
import logging
import sqlite3
import asyncio
import json
import os
from discord.ext import tasks
import twitchio
import aiohttp

intents = discord.Intents.all()  # Set Intents
bot = discord.Bot()  # Create Bot Instance

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

with open("config.json") as config_file:
    config = json.load(config_file)
    token = config["token"]


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")  # Print Logged in as Bot Name (Bot ID)


# Command Handler
commands_folder = "commands"  # Define commands folder

# Load Commands
for filename in os.listdir(commands_folder):
    if filename.endswith(".py"):
        command_name = filename[:-3]  # Remove .py from filename
        try:
            bot.load_extension(f"{commands_folder}.{command_name}")
            print(f"Loaded {command_name} command")
        except Exception as e:
            print(f"Failed to load {command_name} command: {e}")

        # Load Data from the database
        # Implement logic to check Streams periodically
        # Notify users when a streamer goes live


async def is_twitch_channel_live(username, config):
    try:
        # Read Twitch Client ID and OAuth Token from config
        client_id = config.get('TWITCH_CLIENT_ID')
        oauth_token = config.get('TWITCH_OAUTH_TOKEN')

        if not client_id or not oauth_token:
            print("Twitch Client ID and OAuth Token not found in config.json")
            return False, None

        # Create a session for making HTTP requests
        async with aiohttp.ClientSession() as session:
            # Get the user ID for the Twitch username
            async with session.get(f'https://api.twitch.tv/helix/users?login={username}',
                                   headers={'Client-ID': client_id,
                                            'Authorization': f'Bearer {oauth_token}'}) as response:
                user_data = await response.json()
                user_id = user_data['data'][0]['id']

            # Check if the user is live
            async with session.get(f'https://api.twitch.tv/helix/streams?user_id={user_id}',
                                   headers={'Client-ID': client_id,
                                            'Authorization': f'Bearer {oauth_token}'}) as response:
                stream_data = await response.json()
                is_live = len(stream_data['data']) > 0

            if is_live:
                return True, f'https://twitch.tv/{username}'
    except Exception as e:
        print(f"Error checking Twitch stream: {e}")

    return False, None


@tasks.loop(minutes=5)  # Adjust the interval as needed (e.g., 5 minutes)
async def check_twitch_streams():
    conn = sqlite3.connect('live-notify.db')
    cursor = conn.cursor()

    cursor.execute('SELECT user_id, twitch_username, notify_channel_id, notify_role_id FROM twitch_users')
    rows = cursor.fetchall()

    for row in rows:
        user_id, twitch_username, notify_channel_id, notify_role_id = row

        is_live, twitch_url = await is_twitch_channel_live(twitch_username)

        if is_live:
            # Notify in the specified channel and mention the role
            channel = bot.get_channel(notify_channel_id)
            role = discord.utils.get(channel.guild.roles, id=notify_role_id)

            if channel and role:
                message = f"{role.mention} {user_id} is live on Twitch! Check them out: {twitch_url}"
                await channel.send(message)

    conn.close()


@check_twitch_streams.before_loop
async def before_check_twitch_streams():
    await bot.wait_until_ready()


# Database Handling and notifications here

# start the loop
check_twitch_streams.start()

bot.run(token)  # Run Bot
