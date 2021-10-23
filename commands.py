
from collections import namedtuple
from names import get_name
from smiles import get_smile
from locations import get_country

import random

Command = namedtuple("Command", "name aliases function")

commands = {
    "who": Command("who", {"who", "who's", "whomst", "whose"}, get_name),
    "smile": Command("smile", {"smile", "kiss"}, get_smile),
    "where": Command("where", {"where", "where's", "which country"}, get_country)
}