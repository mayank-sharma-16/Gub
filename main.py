import discord
import os
import asyncio

from dotenv import load_dotenv

from discord.ext import commands
from questions import Questions
from ythandle import Music


import random

load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")

bot = commands.Bot(command_prefix=["gub ", "Gub ", "gub", "GUB "])

intents = discord.Intents.all()

bot.add_cog(Questions(bot))
bot.add_cog(Music(bot))

bot.run(DISCORD_KEY)