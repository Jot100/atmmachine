import discord
import csv
from datetime import datetime

# Initialize the Discord client with intents
intents = discord.Intents.default()
intents.members = True  # Enable the member-related events

client = discord.Client(intents=intents)

# Event triggered when a member joins the server
@client.event
async def on_member_join(member):
    # Open the CSV file in append mode
    with open('user_list.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the member's username and join date to the CSV
        writer.writerow([member.name, datetime.now()])

# Event triggered when a member leaves the server
@client.event
async def on_member_remove(member):
    # Read the existing user list from the CSV file
    with open('user_list.csv', 'r') as file:
        reader = csv.reader(file)
        user_list = list(reader)

    # Create a new list with users that should be kept
    updated_user_list = [user for user in user_list if user[0] != member.name]

    # Write the updated user list back to the CSV file
    with open('user_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_user_list)

# Run the Discord bot
client.run('YOUR_DISCORD_BOT_TOKEN')




