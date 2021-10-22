import discord
import os

from dotenv import load_dotenv
from messages import READY_MESSAGE, DEFAULT_GREETINGS, NAMES
from insults import get_insult
import random


load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")


class MyClient(discord.Client):

    async def on_ready(self):
        print(READY_MESSAGE)

    async def on_message(self, message):

        message_list = message.content.split(' ')

        if len(message.content) > 0 and message.content[:3].lower() == "gub":

            if len(message.content.split()) > 1:

                if (message_list[1].lower == "who" or message_list[1] == "who's") and message.content[-1] == "?":
                    await message.channel.send(random.choice(NAMES))

                elif message_list[1].lower == "smile":
                    await message.channel.send(file=discord.File('gub.png'))

                elif message.author.name in DEFAULT_GREETINGS.keys():
                    #default = DEFAULT_GREETINGS[message.author.name]
                    gen = get_insult()
                    await message.channel.send(next(gen))

            elif message.author.name != 'Gub':
                await message.channel.send("I don't know who you are but if you know what's good for you, you'll leave your slugs by the door.")

client = MyClient()
client.run(DISCORD_KEY)