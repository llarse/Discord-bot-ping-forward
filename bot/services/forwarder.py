import json
import discord

from services.message_formatter import format_message

def load_forwards():
    try:
        with open("bot/data/forwards.json", "r") as f:
            forwards = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Issue with Forwards storage - Resetting forwards")
        forwards = {}
        save_forwards(forwards)
    return forwards

def save_forwards(forwards):
    with open("bot/data/forwards.json", "w") as f:
        json.dump(forwards, f, indent=4)

def add_dm_forward(forward_from: str, dm_id: str):
    # Load forwards
    forwards = load_forwards()
    # Typecast to avoid python key matching issues
    forward_from = str(forward_from)

    # If a config exists, import it
    if forward_from in set(forwards.keys()):
        config = forwards[forward_from]
    # If not, create a blank one
    else:
        config = {
            "forwardToIDs": [],
            "forwardToChannels": None
        }

    # Add dm to forward to to config
    if dm_id not in config["forwardToIDs"]:
        config["forwardToIDs"].append(dm_id)

    forwards[forward_from] = config
    save_forwards(forwards)
    return config

async def send_forward(bot, message, config):
    ''' Initiate forwarding - Currently only forwards to dms'''
    ids_to_dm = config["forwardToIDs"]
    for user_id in ids_to_dm:
        await forward_dm(bot, message, user_id)
    
async def forward_dm(bot, message, user_id):
    """Forwards the given message to the user specified by user_id via DM."""

    try:
        user = await bot.fetch_user(user_id)
    except (discord.errors.NotFound, discord.HTTPException, discord.errors.Forbidden) as e:
        # User not found or other HTTP errors during fetching
        await message.channel.send(f"An error occurred while fetching the user for DM: {e}")
        return

    try:
        dm_channel = await user.create_dm()
    except (discord.HTTPException, discord.errors.Forbidden) as e:
        # Error creating DM channel (e.g., bot cannot DM user)
        await message.channel.send(f"Could not forward a DM for {message.author.name} because: {e}")
        return

    try:
        return_message = format_message(message)
        await dm_channel.send(return_message)
    except (discord.HTTPException, discord.errors.Forbidden) as e:
        # Error sending the DM (e.g., rate limiting)
        await message.channel.send(f"An error occurred while sending the DM for {message.author.name}: {e}")

async def handle_dm_reply(bot, message):
    if message.reference and message.reference.message_id:
        # Fetch the original forwarded message
        try:
            original_forwarded_message = await message.channel.fetch_message(message.reference.message_id)
        except discord.NotFound:
            print("Original forwarded message not found")
            return
        
        # Extract the original message URL from the content of the original forwarded message
        original_message_url = None
        for line in original_forwarded_message.content.split("\n"):
            if line.startswith("[Jump to message]("):
                original_message_url = line.split("[Jump to message](")[1].split(")")[0].strip()
                break
        
        if not original_message_url:
            print("Original message URL not found in the forwarded message")
            return
        
        # Extract guild ID, channel ID, and message ID from the URL
        parts = original_message_url.split('/')
        guild_id = int(parts[4])
        channel_id = int(parts[5])
        message_id = int(parts[6])
        
        # Fetch the original message
        guild = bot.get_guild(guild_id)
        if not guild:
            print(f"Guild with ID {guild_id} not found")
            return
        
        channel = guild.get_channel(channel_id)
        if not channel:
            print(f"Channel with ID {channel_id} not found in guild {guild_id}")
            return
        
        try:
            original_message = await channel.fetch_message(message_id)
        except discord.NotFound:
            print(f"Original message with ID {message_id} not found in channel {channel_id}")
            return
        
        # Send the reply to the original channel
        reply_content = (
            f"**Reply**:\n{message.content}\n\n"
        )
        await original_message.reply(reply_content)