import discord

async def get_smile(message):
    await message.channel.send(file=discord.File('images/gub.png'))