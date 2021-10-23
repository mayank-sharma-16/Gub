
from collections import namedtuple
from names import get_name
from smiles import get_smile
from locations import get_country
from hypotheticals import get_binary

import random

Command = namedtuple("Command", "name aliases function")

commands = {
    "who": Command("who", {"who", "who's", "whomst", "whose"}, get_name),
    "smile": Command("smile", {"smile", "kiss"}, get_smile),
    "where": Command("where", {"where", "where's", "which country"}, get_country),
    "is": Command("is", {"is", "would", "can", "will", "are", "did", "could", "should", "do"}, get_binary),
}