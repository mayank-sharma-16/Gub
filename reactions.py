import discord
import random
from constants import HAPPY_REACT_FILE_PATHS, SAD_REACT_FILE_PATHS

async def happy_react(message):
    await message.channel.send(file=discord.File(random.choice(HAPPY_REACT_FILE_PATHS)))

async def sad_react(message):
    await message.channel.send(file=discord.File(random.choice(SAD_REACT_FILE_PATHS)))