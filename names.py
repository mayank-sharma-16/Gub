import random
from constants import NAMES

async def get_name(message):
    await message.channel.send(random.choice(NAMES))