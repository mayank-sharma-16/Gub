from discord.ext import commands
import discord
import random
from constants import NAMES, GUB_PRAISES, GUB_INSULTS, HAPPY_REACT_FILE_PATHS, SAD_REACT_FILE_PATHS, DAYS, SELF_FILE_PATH
from locations import get_country

class Questions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Gub has arisen")

    @commands.Cog.listener(name="on_message")
    async def react_to_praise(self, message):
        
        if message.content in GUB_PRAISES:
            await message.channel.send(file=discord.File(random.choice(HAPPY_REACT_FILE_PATHS)))
        elif message.content in GUB_INSULTS:
            await message.channel.send(file=discord.File(random.choice(SAD_REACT_FILE_PATHS)))

    @commands.command(name="smile")
    async def smile(self, ctx):
        await ctx.send(file=discord.File(SELF_FILE_PATH))

    @commands.command(name="to_be", aliases=["will", "is", "should", "could", "would", "can", "are", "did", "does", "do"])
    async def to_be(self, ctx):
        if random.random() > 0.5:
            await ctx.send("Yes")
        else:
            await ctx.send("No")

    @commands.command(name="who", aliases=["which of us", "who's", "whose"])
    async def who(self, ctx):
        await ctx.send(random.choice(NAMES))

    @commands.command(name="when", aliases=["when's"])
    async def when(self, ctx):
        if random.random()>0.5:
            await ctx.send(f'{random.randint(0,4500)}AD')
        else:
            await ctx.send(f'{random.choice(DAYS)}')

    @commands.command(name="where", aliases=["where's","which country"])
    async def where(self, ctx):
        await ctx.send(get_country())

    @commands.command(name="test")
    async def test(self, ctx, echo="Gub reporting for duty."):
        await ctx.send(echo)
