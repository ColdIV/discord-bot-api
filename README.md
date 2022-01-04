# API
**Requires Python 3.7 or higher!**

*Which means you may have to compile Python yourself on RaspbianOS*

This API enables you to trigger a bot sending posts to a Discord channel by sending POST requests to a website.

GET requests are not implemented but easily added.

# Setup
    git clone https://github.com/ColdIV/discord-bot-api
    cd discord-bot-api
    virtualenv env
### Linux
    source env/bin/activate
### Windows
    .\env\Scripts\activate
### Install requirements    
    pip3 install -r requirements.txt
### Add tokens and channel id
Rename `.config.example` to `.config` and fill in the tokens and channel id.

You should then have a file that looks something like this:

    [api]
    TOKEN=EXAMPLE_API_TOKEN
    
    [discord]
    TOKEN=EXAMPLE_DISCORD_BOT_TOKEN
    CHANNEL_ID=EXAMPLE_DISCORD_CHANNEL_ID

## Run dev
    python3 api.py
## Run prod
    hypercorn api:app
    
# Usage
Send a post request with 

    token=EXAMPLE_DISCORD_BOT_TOKEN&message=EXAMPLE_MESSAGE


The tokens should, of course, never be published. :)
