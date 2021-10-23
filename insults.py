import random
from constants import SHAKESPEARE_FILE_PATH, ANIMALS_FILE_PATH

def get_insult(message):

    f = open(SHAKESPEARE_FILE_PATH)
    g = open(ANIMALS_FILE_PATH)

    insults = [line for line in f]
    animals = [line for line in g]

    f.close()
    g.close()

    while True:
        insult = f"you {random.choice(insults).strip().lower()} {random.choice(animals).strip().lower()}"
        yield insult
