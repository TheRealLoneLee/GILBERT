import discord 
import logging
import sqlite3
import json
import os

intents = discord.Intents.all() # Set Intents

bot = discord.Bot() # Create Bot Instance


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
  print(f"Logged in as {bot.user.name} ({bot.user.id})") # Print Logged in as Bot Name (Bot ID)
    

# Command Handler
commands_folder = "commands" # Define commands folder

# Load Commands
for filename in os.listdir(commands_folder):
  if filename.endswith(".py"):
    command_name = filename[:-3] # Remove .py from filename
    try:
      bot.load_extension(f"{commands_folder}.{command_name}")
      print(f"Loaded {command_name} command")
    except Exception as e:
      print(f"Failed to load {command_name} command: {e}")

  
    # Load Data from the database
    # Implement logic to check Streams periodically
    # Notify users when a streamer goes live


@tasks.loop(seconds=5)
async def check_twitch_streams():
  # Check Twitch streams and send notifications if live
  pass

@check_twitch_streams.before_loop
async def before_check_twitch_streams():
  await bot.wait_until_ready()
  
# Database Handling and notifications here

#start the loop
check_twitch_streams.start()


bot.run(token) # Run Bot