import discord
import json
import asyncio
import sqlite3
from discord.ext import commands

# Load the Twitch Client ID from config.json
with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
twitch_client_id = config_data["TWITCH_CLIENT_ID"]

class NotifyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def notify(self, ctx):
        # Ask for a Twitch Username
        await ctx.send("What is your Twitch Username?")

        def check(message):
            return message.author == ctx.author

        try:
            twitch_username_msg = await self.bot.wait_for('message', check=check, timeout=60.0)
            twitch_username = twitch_username_msg.content.strip()

            # Generate the OAuth URL
            oauth_url = f"https://id.twitch.tv/oauth2/authorize?client_id={twitch_client_id}&redirect_uri=http://localhost&response_type=token&scope=user:read:email+channel:read:subscriptions+channel:read:redemptions+channel_subscriptions+user_read_broadcast+user_read_email+user_follows_edit+chat:read+chat:edit+whispers:read+whispers:edit&state={twitch_username}"

            await ctx.send(f"Please visit this URL to authorize the bot: {oauth_url}")

            # Wait for the user to complete the OAuth authorization
            await ctx.send("After authorizing the bot, please enter the OAuth token:")

            try:
                # Wait for a message with the OAuth token
                oauth_token_msg = await self.bot.wait_for('message', check=check, timeout=600.0)
                oauth_token = oauth_token_msg.content.strip()

                # Ask for a Role ID to ping
                await ctx.send("Please enter the Role ID to ping:")

                try:
                    # Wait for a message with the role ID
                    role_id_msg = await self.bot.wait_for('message', check=check, timeout=60.0)
                    notify_role_id = int(role_id_msg.content.strip())

                    # Store the data in the SQLite database, including the OAuth token
                    conn = sqlite3.connect('live-notify.db')
                    cursor = conn.cursor()

                    user_id = ctx.author.id

                    # Insert data into the table, including the OAuth token
                    cursor.execute('''
                        INSERT INTO twitch_users (user_id, twitch_username, notify_role_id, oauth_token)
                        VALUES (?, ?, ?, ?)
                    ''', (user_id, twitch_username, notify_role_id, oauth_token))

                    # Commit the changes and close the connection
                    conn.commit()
                    conn.close()

                    await ctx.send("Successfully added you to the notify list!")

                except ValueError:
                    await ctx.send("Invalid Role ID. Please enter a valid Role ID.")
                except asyncio.TimeoutError:
                    await ctx.send("You took too long to respond for the Role ID.")

            except asyncio.TimeoutError:
                await ctx.send("You took too long to respond for the OAuth token.")
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond for the Twitch Username.")

def setup(bot):
    bot.add_cog(NotifyCommand(bot))
