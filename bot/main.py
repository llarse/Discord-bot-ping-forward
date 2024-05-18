import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(BOT_TOKEN)