import random 

async def get_country(message):
    f = open('files/countries.txt')
    countries = f.readline().split(',')
    f.close()
    await message.channel.send(random.choice(countries))