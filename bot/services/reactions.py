import discord

async def add_checkmark(message):
    """ Adds a checkmark reaction to a message """

    checkmark_emoji = "✅"  # Unicode for checkmark emoji
    try:
      await message.add_reaction(checkmark_emoji)  # Use default unicode emoji
    except discord.HTTPException as e:
      print(f"Error adding checkmark reaction: {e}")
