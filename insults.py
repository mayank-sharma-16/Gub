import random

def get_insult():

    i = 0

    f = open("shake_insults.txt")
    g = open("animals.txt")

    insults = [line for line in f]
    animals = [line for line in g]

    while True:
        insult = f"you {random.choice(insults).strip().lower()} {random.choice(animals).strip().lower()}"
        yield insult
