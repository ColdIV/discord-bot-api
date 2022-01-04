# API
**Requires Python 3.7 or higher**

*Which means you may have to compile Python yourself on RaspbianOS*

# Setup
    git clone https://github.com/ColdIV/discord-bot-api
    cd discord-bot-api
    virtualenv env
## Linux
    source env/bin/activate
## Windows
    .\env\Scripts\activate
# Install requirements    
    pip3 install -r requirements.txt
# Create token files
BOT_TOKEN

    <token of the discord bot>
API_TOKEN

    <token of the api>
# Run dev
    python3 api.py
# Run prod
    hypercorn api:app
    
# Usage
Send a post request with 

    token=<token of the api>&message=<message you want to post in discord>


The API Token should, of course, never be published. :)
