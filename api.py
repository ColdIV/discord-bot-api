import discord
from discord.ext import commands, tasks
from quart import Quart, request
import os

# Read bot token from file
BOT_TOKEN = ""
BOT_TOKEN_FILE = 'BOT_TOKEN'
import os.path
if os.path.isfile(BOT_TOKEN_FILE):
    with open(BOT_TOKEN_FILE, 'r') as file:
        BOT_TOKEN = file.read()

# Read api token from file   
API_TOKEN = ""
API_TOKEN_FILE = 'API_TOKEN'
import os.path
if os.path.isfile(API_TOKEN_FILE):
    with open(API_TOKEN_FILE, 'r') as file:
        API_TOKEN = file.read()     

# Create bot "client"
client = commands.Bot(command_prefix = '!')

# app = Webserver
app = Quart(__name__)

@app.route('/api-test', methods=['GET'])
async def apiTest():
    return "<form action='/' method=post><input name=token value=testtoken><input name=message value=testmessage><input type=submit value=submit></form>"
    
@app.route('/', methods=['GET'])
async def indexGet():
    return "false"
    
@app.route('/', methods=['POST'])
async def index():
    # Get token and message from form
    token = (await request.form)["token"]
    message = (await request.form)["message"]
    
    print ("[LOG] TOKEN: '" + token + "'")
    print ("[LOG] MESSAGE: '" + message + "'")
    
    if token != API_TOKEN:
        print ("[LOG] ERROR - Invalid token")
        # Returns false on error (invalid token)
        return "false"
   
    global client
    # Parameter is Channel ID
    channel = client.get_channel(926830382769393685)
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