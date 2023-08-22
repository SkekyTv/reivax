# Import the os module.
import os

# This example requires the 'message_content' intent.
import discord
from discord.ext import commands


# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv

# Import cog
from music_cog import music_cog

# Loads the .env file that resides on the same level as the script.
load_dotenv()

# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', description='basic bot', intents=intents)


@bot.event
async def on_ready():
    await bot.add_cog(music_cog(
        bot,
        default_voice_channel=os.getenv("DEFAULT_VOICE_CHANNEL"),
        default_server = os.getenv("DEFAULT_SERVER")
    ))
    print(f'We have logged in as {bot.user}')

# Start the bot
bot.run(DISCORD_TOKEN)


