import json
import discord

def load_forwards():
    try:
        with open("bot/data/forwards.json", "r") as f:
            forwards = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error - Resetting forwards")
        forwards = {}
        save_forwards(forwards)
    return forwards

def save_forwards(forwards):
    with open("bot/data/forwards.json", "w") as f:
        json.dump(forwards, f, indent=4)

def add_dm_forward(forward_from: str, dm_id: str):
    forwards = load_forwards()
    forward_from = str(forward_from)
    if forward_from in set(forwards.keys()):
        config = forwards[forward_from]
    else:
        config = {
            "forwardToIDs": [],
            "forwardToChannels": None
        }

    if dm_id not in config["forwardToIDs"]:
        config["forwardToIDs"].append(dm_id)

    forwards[forward_from] = config
    save_forwards(forwards)
    return config

async def send_forward(bot, message, config):
    ids_to_dm = config["forwardToIDs"]
    for user_id in ids_to_dm:
        try:
            user = await bot.fetch_user(user_id)
            dm_channel = await user.create_dm()
            # For now, return message will just be message content to confirm bots functionallity
            return_message = message.content
            await dm_channel.send(return_message)
        except discord.errors.NotFound:
            await message.channel.send(f'Could not forward a DM for {message.author.name} because the user to DM was not found')
        except discord.errors.Forbidden:
            await message.channel.send(f'Could not forward a DM for {message.author.name} because the user to DM was not able to receive a DM from the bot')
