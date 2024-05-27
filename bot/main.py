import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

from services.forwarder import add_dm_forward, load_forwards, send_forward
from services.reactions import add_reaction_emoji

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Load forwards.json
forwards = load_forwards()
# Create set from keys for 0(1) lookups
forward_ids = set(forwards.keys())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(name='add-forward')
async def add_forward(ctx, dm_id=None):
    # If no id to dm is provided, dm the author
    if dm_id == None:
        dm_id = str(ctx.author.id)
    config = add_dm_forward(ctx.author.id, dm_id)

    # Add to cache
    forwards[ctx.author.id] = config
    forward_ids.add(ctx.author.id)
    await ctx.send(f'Added forward for {ctx.author.name} to {dm_id}')

# Listen for Pings
@bot.event
async def on_message(message):
    # Ignore bot
    if message.author == bot.user:
        return
    
    found = False
    for mention in message.mentions:
        if str(mention.id) in forward_ids:
            found = True
            config = forwards[str(mention.id)]
            await send_forward(bot, message, config)
    
    # Add a checkmark once complete
    if found:
        await add_reaction_emoji(message)


bot.run(BOT_TOKEN)