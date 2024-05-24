import discord

async def add_reaction_emoji(message):
    """ Adds a checkmark reaction to a message """

    reaction_emoji = "📨"  # Unicode for checkmark emoji
    try:
      await message.add_reaction(reaction_emoji)  # Use default unicode emoji
    except discord.HTTPException as e:
      print(f"Error adding checkmark reaction: {e}")
