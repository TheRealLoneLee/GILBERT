import os

# Make the initiate.sh script executable
os.system('chmod +x ./initiate.sh')

# Ask the user if they want to initiate the bot
initiate_bot = input("Do you wish to initiate the bot? (Y/N) ")
if initiate_bot.lower() == 'y':
    os.system('initiate.sh')
else:
    print("Understood. Skipping this step. (If you wish to initiate the bot run the initiate.sh script manually.)")
