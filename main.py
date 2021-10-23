import discord
import os
import asyncio

from dotenv import load_dotenv
from constants import READY_MESSAGE, FUCKOFF_MESSAGES
from utils.content_validation import gub_mentioned, gubs_messaged, check_command, gub_praised
from reactions import happy_react, sad_react
from commands import commands

import random


load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")

class MyClient(discord.Client):

    async def on_ready(self):
        print(READY_MESSAGE)

    async def on_message(self, message):

        if not gubs_messaged(message):
            
            if gub_mentioned(message):

                command_name = check_command(message)

                if command_name == None:
                    await message.channel.send(random.choice(FUCKOFF_MESSAGES))
                    return

                else:
                    await asyncio.sleep(1)
                    command_data = commands[command_name]
                    await command_data.function(message)
        
            elif gub_praised(message) == 1:
                await happy_react(message)

            elif gub_praised(message) == 2:
                await sad_react(message)
    

client = MyClient()
client.run(DISCORD_KEY)