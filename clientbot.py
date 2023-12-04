import discord
import csv
from datetime import datetime

# Initialize the Discord client with intents
intents = discord.Intents.default()
intents.members = True  # Enable the member-related events

client = discord.Client(intents=intents)

# Function to load existing user list from CSV
def load_user_list():
    try:
        with open('user_list.csv', 'r') as file:
            reader = csv.reader(file)
            user_list = list(reader)
        return user_list
    except FileNotFoundError:
        return []

# Function to save user list to CSV
def save_user_list(user_list):
    with open('user_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(user_list)

# Event triggered when the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # Load existing user list or create an empty list
    user_list = load_user_list()

    # Add current users to the user list with the current date
    for guild in client.guilds:
        for member in guild.members:
            user_exists = any(user[0] == member.name for user in user_list)
            if not user_exists:
                user_list.append([member.name, str(datetime.now())])

    # Save the updated user list to the CSV
    save_user_list(user_list)

# Event triggered when a member joins the server
@client.event
async def on_member_join(member):
    # Load existing user list
    user_list = load_user_list()

    # Check if the member is already in the user list
    user_exists = any(user[0] == member.name for user in user_list)

    if not user_exists:
        # Add the new member to the user list with the current date
        user_list.append([member.name, str(datetime.now())])

        # Save the updated user list to the CSV
        save_user_list(user_list)

# Event triggered when a member leaves the server
@client.event
async def on_member_remove(member):
    # Load existing user list
    user_list = load_user_list()

    # Remove the member from the user list
    user_list = [user for user in user_list if user[0] != member.name]

    # Save the updated user list to the CSV
    save_user_list(user_list)

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual Discord bot token
client.run('YOUR_DISCORD_BOT_TOKEN')
print(client.event)