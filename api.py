import discord
from discord.ext import commands, tasks
from quart import Quart
import os

# Read bot token from file
TOKEN = ""
TOKEN_FILE = 'BOT_TOKEN'
import os.path
if os.path.isfile(TOKEN_FILE):
    with open(TOKEN_FILE, 'r') as file:
        TOKEN = file.read()

# Create bot "client"
client = commands.Bot(command_prefix = '!')

# app = Webserver
app = Quart(__name__)

@app.route("/")
async def index():
    global client
    # Parameter is Channel ID
    channel = client.get_channel(926830382769393685)
    # Send message to channel
    await channel.send("Hello, World!")
    
    # Returns content of website
    return "true"

@client.event
async def on_ready():
    await client.wait_until_ready()
    print ('Bot is ready.')
    print ('Setting presence...')
    await client.change_presence(status=discord.Status.idle)
    print ('Done.')
    
    # Run Webserver
    client.loop.create_task(app.run_task())

# Run bot
client.run(TOKEN)