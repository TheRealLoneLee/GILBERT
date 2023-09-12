import json
import os
import time

# Create the directory if it doesn't exist
if not os.path.exists('bot'):
    os.makedirs('bot')

# Create a dictionary with the default configuration
config = {
    "token": "[BOT TOKEN]",
    "TWITCH_CLIENT_ID": "[TWITCH APP ID]"
}

# Prompt the user for their Discord bot token
token = input("Please enter your Discord bot token: ")
config["token"] = token

# Ask the user if they want to use Twitch integration
twitch_integration = input("Do you want to use Twitch integration? (Y/N) ")
if twitch_integration.lower() == 'y':
    twitch_client_id = input("Please enter your Twitch application client ID: ")
    config["TWITCH_CLIENT_ID"] = twitch_client_id

# Write the configuration to a JSON file
with open('bot/config.json', 'w') as f:
    json.dump(config, f)

# Wait for a moment to ensure the file is written
time.sleep(1)

# Check if the file was created successfully
if os.path.exists('bot/config.json'):
    print("config.json has been created successfully.")
else:
    print("Failed to create config.json.")

# Make the initiate.sh script executable
os.system('chmod +x ./initiate.sh')

# Ask the user if they want to initiate the bot
initiate_bot = input("Do you wish to initiate the bot? (Y/N) ")
if initiate_bot.lower() == 'y':
    os.system('./initiate.sh')
else:
    print("Understood. Skipping this step. (If you wish to initiate the bot run the initiate.sh script manually.)")
