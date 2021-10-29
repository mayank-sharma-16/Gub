
import random

Command = namedtuple("Command", "name aliases function")

orders = {
    #"who": Command("who", {"who", "who's", "whomst", "whose"}, get_name),
    "smile": Command("smile", {"smile", "kiss"}, get_smile),
    "where": Command("where", {"where", "where's", "which country"}, get_country),
    "is": Command("is", {"is", "would", "can", "will", "are", "did", "could", "should", "do"}, get_binary),
    "when": Command("when", {"when", "when's", "what year"}, get_time),
}