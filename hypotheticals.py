import random

async def get_binary(message):
    if random.random() > 0.5:
        await message.channel.send("Yes")
    else:
        await message.channel.send("No")