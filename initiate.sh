#!/bin/bash
# This script is used to setup the environment for the Gilbert Discord Bot on a Raspberry Model PI 4 4GB
# running Raspbian 10 64-bit. It will check for updates to the bot, Python, and pip. It will also install
# the Pycord, dotenv, twitchio, and aiohttp libraries. Finally, it will prompt the user to run the
# database setup and start the bot.

# Create the directory if it doesn't exist
if [ ! -d "bot" ]; then
    mkdir bot
fi

# Navigate to your bot directory
cd bot

# Check if the repository exists in the directory
if [ ! -d "GILBERT" ]; then
    echo "Repository not found. Cloning..."
    git clone https://github.com/TheRealLoneLee/GILBERT.git GILBERT
else
    echo "Repository found. Checking for updates..."
    cd GILBERT
    git remote update

    # If updates were found, pull them
    if [ $(git status -uno | grep 'Your branch is behind' | wc -l) -gt 0 ]; then
        echo "Updates found. Pulling latest changes..."
        git pull
    else
        echo "No updates found."
    fi
fi

# Create a dictionary with the default configuration
echo '{
    "token": "[BOT TOKEN]",
    "TWITCH_CLIENT_ID": "[TWITCH APP ID]"
}' > config.json

# Prompt the user for their Discord bot token
read -p "Please enter your Discord bot token: " token
sed -i 's/\[BOT TOKEN\]/'"$token"'/' config.json

# Ask the user if they want to use Twitch integration
read -p "Do you want to use Twitch integration? (Y/N) " twitch_integration
if [ "$twitch_integration" = "Y" ] || [ "$twitch_integration" = "y" ]; then
    read -p "Please enter your Twitch application client ID: " twitch_client_id
    sed -i 's/\[TWITCH APP ID\]/'"$twitch_client_id"'/' config.json
fi

# Check if pip is installed and update it if necessary
if command -v pip3 &>/dev/null; then
    echo "pip is installed. Checking for updates..."
    pip3 install --upgrade pip
else
    echo "pip is not installed. Installing..."
    sudo apt install python3-pip
fi

pip3 install pycord # Install the Pycord library
pip3 install python-dotenv # Install the dotenv library
pip3 install twitchio # Install the twitchio library
pip3 install aiohttp # Install the aiohttp library

# Prompt the user before running the database setup
read -p "Do you want to run the database setup? (if no then you will need to manually initiate this on your own.) (Y/N) " answer
case ${answer:0:1} in
    y|Y )
        echo "Running database setup..."
        python3 GILBERT/database_setup.py # Setup the database
    ;;
    * )
        echo "Skipping database setup."
    ;;
esac

# Prompt the user before starting the bot
read -p "Do you want to start the bot? (Y/N) " answer
case ${answer:0:1} in
    y|Y )
        echo "Starting the bot..."
        python3 GILBERT/main.py # Run the bot
    ;;
    * )
        echo "Skipping automatic bot start. (You can start the bot manually by running 'python3 main.py') Enjoy!"
    ;;
esac

# Exit the script

