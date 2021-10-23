
from collections import namedtuple
from names import get_name
from smiles import get_smile

import random

Command = namedtuple("Command", "name aliases function")

commands = {
    "who": Command("who", {"who", "who's", "whomst", "whose"}, get_name),
    "smile": Command("smile", {"smile", "kiss"}, get_smile),
    "where": Command("where", {"where"}, get_country)
}