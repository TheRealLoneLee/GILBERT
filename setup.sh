#!/bin/bash
# This script is used to setup the environment for the Gilbert Discord Bot on PI 4
sudo apt update # Update the system
sudo apt install python3 python3-pip # Install Python 3 and pip
pip3 install pycord # Install the pycord library
pip3 install python-dotenv # Install the dotenv library
pip3 install twitchio # Install the twitchio library
pip3 install aiohttp # Install the aiohttp library

python3 database_setup.py # Setup the database