import logging
import sys
import os
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive!"

print("Python Path: ", sys.path)
print("Current Working Directory: ", os.getcwd())

try: 
    import discord
    from discord.ext import commands
    from discord import Embed
    print("Discord Version: ", discord.__version__ )
except Exception as e: 
        print("Import Error ", str(e))
        print("Python Version: ", sys.version)
        raise

logging.basicConfig(level=logging.INFO)
print(os.getcwd())

# Start the bot in a separate thread so the webserver can keep responding
def run_discord_bot():
    #Initialize bots
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix = "!", intents = intents, shard_count = 1)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')
        #bot.load_extension('cogs.GoToSleep')
        await bot.load_extension('cogs.minimal')
        try:
            await bot.load_extension('cogs.haiku_count')
            print('Haiku cog loaded successfully!')
        except Exception as e:
            print(f'Failed to load example cog: {e}')
        print(f'Loaded Extensions: {bot.cogs}')

    bot.run('MTI4MzY2MDM0NzY1NTMyMzczMA.GngPeb.uC_srlCE5rGYC1C9RjEGADSIot_NEk-iJNLENY')
    #Token = MTI4MzY2MDM0NzY1NTMyMzczMA.GngPeb.uC_srlCE5rGYC1C9RjEGADSIot_NEk-iJNLENY (We love security here. )

if __name__ == "__main__":
    # Start the discord bot in a separate thread
    threading.Thread(target=run_discord_bot).start()
    # Then start the Flask app
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)


