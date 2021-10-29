import asyncio
import discord
import validators
from discord.ext import commands
from discord import Spotify
from ytdlsource import YTDLSource
from youtube_search import YoutubeSearch

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = []

    @commands.command(name="join")
    async def join(self, ctx):

        voice = ctx.author.voice
        if voice is None or ctx.author.voice.channel is None:
            return await ctx.send('Get in a channel first idiot')

        channel = ctx.author.voice.channel

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
            
        await channel.connect()

    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, *, url=""):
        """Streams from a url (same as yt, but doesn't predownload)"""

        if ctx.voice_client is not None and ctx.voice_client.is_paused() and url is "":
            return await ctx.voice_client.resume()

        elif url is "":
            return await ctx.send("Nothing to play")

        elif url is not validators.url(url):
            results = YoutubeSearch(url, max_results=1).to_dict()
            url = f"https://www.youtube.com{results[0]['url_suffix']}"

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
            await asyncio.sleep(1)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def pause(self, ctx):

        voice_client = ctx.message.guild.voice_client
        if ctx.voice_client is not None or voice_client.is_playing():
            await ctx.voice_client.pause()
        else:
            await ctx.send("Nothing's playing.")

    @commands.command()
    async def spot(self, ctx):

        print('spot')

        user = ctx.author
        for activity in user.activities:
            if isinstance(activity, Spotify):
                await ctx.send(f"{activity.artist}")



    


    