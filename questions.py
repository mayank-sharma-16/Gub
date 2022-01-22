from discord.ext import commands
import discord
import random
from pathlib import Path
from constants import NAMES, ANIMAL_NAMES, ANIMAL_ALIASES, STORE_ALIASES, STORE_NAMES, DOG_ALIASES, DOG_NAMES, GUB_PRAISES, GUB_INSULTS
from constants import HAPPY_REACT_FILE_PATHS, SAD_REACT_FILE_PATHS, DAYS, SELF_FILE_PATH, DOGS_FILE_PATH, JOKER_REACT_FILE_PATHS, ANGRY_REACT_FILE_PATHS
from constants import GUB_GREETINGS, DEFAULT_GREETINGS, FUCKOFF_MESSAGES, JOKER_MESSAGES, SHITTY_SEX_MESSAGES, HORNY_REACT_FILE_PATHS
#from constants import GUB_HUB_CHANNEL_ID
from locations import get_country

class Questions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #self.history = []

    @commands.Cog.listener()
    async def on_ready(self):
        print("Gub has arisen")

    @commands.Cog.listener(name="on_message")
    async def react_to_praise(self, message):

        #print(message.author.name, message.author.id)
        if message.content in GUB_PRAISES:
            #p = Path(random.choice(HAPPY_REACT_FILE_PATHS)+'.jpeg')
            #if p.exists:
            await message.channel.send(file=discord.File(random.choice(HAPPY_REACT_FILE_PATHS)))  
        elif message.content in GUB_INSULTS:
            await message.channel.send(file=discord.File(random.choice(SAD_REACT_FILE_PATHS)))
        elif message.content in GUB_GREETINGS:
            await message.channel.send(f'{random.choice(FUCKOFF_MESSAGES)}')

    @commands.command(name="make")
    async def make(self, ctx):
        if ctx.message.content == "gub make me cum":
            await ctx.send(file=discord.File(random.choice(HORNY_REACT_FILE_PATHS)))
            await ctx.send(random.choice(SHITTY_SEX_MESSAGES))
    
    @commands.command(name="mad")
    async def mad(self, ctx):
        await ctx.send(file=discord.File(random.choice(ANGRY_REACT_FILE_PATHS)))

    @commands.command(name="smile", aliases=["Smile", "SMILE"])
    async def smile(self, ctx):
        await ctx.send(file=discord.File(SELF_FILE_PATH))

    @commands.command(name="laugh", aliases=["Laugh", "LAUGH"])
    async def laugh(self, ctx):
        await ctx.send(file=discord.File(random.choice(JOKER_REACT_FILE_PATHS)))
        await ctx.send(random.choice(JOKER_MESSAGES))

    @commands.command(name="to_be", aliases=["will", "is", "should", "could", "would", "can", "are", "did", "does", "do", "am", "was", "has"])
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

    @commands.command(name="what", aliases=["What", "WHAT", "what's", "which", "Which"])
    async def what(self, ctx):
        split_content = ctx.message.content.split(' ')
        if len(split_content) > 2:
            second = split_content[2]
            if second in ANIMAL_ALIASES:
                await ctx.send(f'{random.choice(ANIMAL_NAMES)}')
            if second in STORE_ALIASES:
                await ctx.send(f'{random.choice(STORE_NAMES)}')
            if second in DOG_ALIASES:
                await ctx.send(f'{random.choice(DOG_NAMES)}')

    '''@commands.command(name="fetch")
    async def fetch(self, ctx):
        if ctx.message.author.id == 545011450159169577:
            self.history = [msg async for msg in ctx.message.channel.history(limit=100)]
            print("fetched")
        else:
            print(f"attempt by {ctx.message.author.id}")

    @commands.command(name="remember", aliases=["recall", "Remember", "REMEMBER"])
    async def remember(self, ctx):
        await ctx.send(self.history[1])'''