def format_message(message):
    # Base URL format to create a link to the message
    base_url = f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}"
    
    # Header with author and link to the message
    formatted_message = (
        f"**Message from {message.author.name}#{message.author.discriminator}**\n"
        f"[Jump to message]({base_url})\n\n"
    )

    # Adding the original message content
    if message.content:
        formatted_message += f"**Content:**\n{message.content}\n\n"

    # Adding any embeds
    if message.embeds:
        formatted_message += "**Embeds:**\n"
        for embed in message.embeds:
            formatted_message += embed_to_str(embed) + "\n"

    # Adding any attachments
    if message.attachments:
        formatted_message += "**Attachments:**\n"
        for attachment in message.attachments:
            formatted_message += f"[{attachment.filename}]({attachment.url})\n"

    return formatted_message

def embed_to_str(embed):
    """Helper function to convert an embed object to a string."""
    embed_str = ""
    if embed.title:
        embed_str += f"**Title:** {embed.title}\n"
    if embed.description:
        embed_str += f"**Description:** {embed.description}\n"
    for field in embed.fields:
        embed_str += f"**{field.name}:** {field.value}\n"
    if embed.footer and embed.footer.text:
        embed_str += f"**Footer:** {embed.footer.text}\n"
    if embed.image:
        embed_str += f"**Image:** [Link]({embed.image.url})\n"
    if embed.thumbnail:
        embed_str += f"**Thumbnail:** [Link]({embed.thumbnail.url})\n"
    if embed.url:
        embed_str += f"**URL:** {embed.url}\n"
    if embed.author:
        embed_str += f"**Author:** {embed.author.name}\n"
    return embed_str


