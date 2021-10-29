import discord
import random
from constants import DAYS

async def get_time(message):
    value = ""
    if random.random() > 0.5:
        value = get_year()
    else:
        value = get_day()
    await message.channel.send(value)

def get_year(start=0, end=4500):
    return random.randint(start, end)

def get_day():
    return random.choice(DAYS)