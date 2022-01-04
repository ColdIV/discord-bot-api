import discord
from discord.ext import commands, tasks
from quart import Quart, request
import os
import configparser

config = configparser.RawConfigParser()
config.read('.config')

# Read tokens and channel id from config
BOT_TOKEN = config['discord']['TOKEN']
CHANNEL_ID = config['discord']['CHANNEL_ID']
API_TOKEN = config['api']['TOKEN']

# Convert CHANNEL_ID to Number
CHANNEL_ID = int(CHANNEL_ID)

# Create bot "client"
client = commands.Bot(command_prefix = '!')

# app = Webserver
app = Quart(__name__)

@app.route('/', methods=['GET'])
async def indexGet():
    return "false"
    
@app.route('/', methods=['POST'])
async def index():
    # Get token and message from form
    token = (await request.form)["token"]
    message = (await request.form)["message"]
    
    # print ("[LOG] TOKEN: '" + token + "'")
    print ("[LOG] MESSAGE SENT: '" + message + "'")
    
    if token != API_TOKEN:
        print ("[LOG] ERROR - Invalid token")
        # Returns false on error (invalid token)
        return "false"
   
    global client
    # Parameter is Channel ID
    channel = client.get_channel(CHANNEL_ID)
    # Send message to channel
    await channel.send(message)
    
    print ("[LOG] SUCCESS")
    # Returns true on success
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
client.run(BOT_TOKEN)