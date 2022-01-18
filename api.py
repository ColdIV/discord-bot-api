import discord
from discord.ext import commands, tasks
from quart import Quart, request
import os
import configparser

config = configparser.RawConfigParser()
config.read('.config')

BOT_TOKEN = config['discord']['TOKEN']
CHANNEL_ID = config['discord']['CHANNEL_ID']
API_TOKEN = config['api']['TOKEN']

CHANNEL_ID = int(CHANNEL_ID)

client = commands.Bot(command_prefix = '!')

app = Quart(__name__)


async def sendMessage (token, message):
    if token != API_TOKEN:
        return '{ "success": false }'
    
    global client
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(message)

    return '{ "success": true }'

@app.route('/', methods=['GET'])
async def indexGet():
    token = request.args.get('token')
    message = request.args.get('message')

    return await sendMessage(token, message)
    
@app.route('/', methods=['POST'])
async def index():
    token = (await request.form)['token']
    message = (await request.form)['message']

    return await sendMessage(token, message)

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