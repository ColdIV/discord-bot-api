# API

# Setup
    git clone https://github.com/ColdIV/minecraft-discord-bot-api
    cd minecraft-discord-bot-api
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