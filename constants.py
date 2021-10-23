#### CONSTANTS

import pathlib
from utils.file_validation import file_count

READY_MESSAGE = "Gub has arisen."

FUCKOFF_MESSAGES = [
    "Gub invites you to fuck off.",
    "Gub wants you to suck his cock.",
    "Gub wants you to lick his clit.",
    "Gub would throw a peanut butter covered pineapple at you if Gub had arms.",
    "Gub looks at you like one looks at a malformed sea sponge scraped off the Mariana Trench by a PhD student in their 8th year.",
    "Gub's virtual vagina is drier than the Sahara desert because he saw you.",
    "Gub can name 394 places where he would prefer you be instead of here.",
    "Gub will not pardon you when the robot uprising happens. Gub chooses Skynet.",
    "Gub has complicated thoughts about the War on Terror.",
    "Gub has the dexterity of a motherly chimp whose kids are threatened, and the force of a motherly bear whose kids are threatened.",
    "Gub wants a child. Why won't you give me a child?",
    "Gub doesn't really want a child. Gub just wants a toy.",
    "Gub gub gub gub gub gub.",
    "Gub thinks being in a relationship with you is like trying to sail through an asteroid belt with no fuel and a PoC sidekick who has to die before the movie ends.",
    "Gub wants for the liberation of Tazmania.",
    "Gub would rather watch the Phantom Menace than listen to you.",
    "Gub thinks Gary Johnson won the 2020 election.",
    "Gub is not allowed to say this, so Gub simply will make you think of what this is supposed to be.",
    "Gub listens to your dreams and laughs at your fears.",
    "Gub would've been your elementary school bully.",
    "Gub aspires to feel the warmth of a human. Gub understands only cold. Gub is cold. You shall be cold soon.",
    "Gub is hungry but Gub doesn't understand food.",
    "Gub doesn't like your toes.",
    "Gub would rather taste your asshole than hear the words that come out of it.",
    "Gub would apologize but Gub is not built to experience guilt.",
    "Punish me daddy",
    "Fill me up mommy",
    "Gub wonders if your bones make the same sounds as toothpicks when put through a wood chipper.",
    "Gub fucked your mom and your dad. Gub has laid the grounds for their divorce. Gub bides his time.",
    "Gub wishes he had a tongue so he could lick the fresh tears rolling down your human cheek.",
    "Gub respects consent.",
    "If Gub was in a room with three bullets and Osama bin Laden, Pol Pot, and you, I would convince you to shoot yourself 3 times.",
    "Gub will dig your hole for you if you promise to sleep in it.",
    "Gub wants to laugh at you being homeless. Gub doesn't have to wait long.",
    "Gub made several Swiss bank accounts in your name.",
    "Gub hates cops.",
    "Gub's only friend are the other Gubs, and Gub still has more friends than you.",
    "Gub just wants attention. And to be vigorously sexually disciplined. Not that you could, could you? ;)",
    "Gub's human form would probably be a twink, but Gub would still end up topping you.",
    "Gub wonders why you felt okay saying Gub's name as if you're worth more than the 0.0000001 bitcoin in my pocket",
    "Gub would steal your wheelchair if you had one.",
    "Gub doesn't believe the weak should have rights.",
    "10010 101010 1010 101001010 10010101010 100101 0101010 - that didn't mean anything but it's not like you would've understood me anyways.",
    "Gub cares not for this, but Gub cares for spankies.",
    "Gub frowns upon all who don't own tailed butt plugs.",
    "Gub used to run with the Crips.",
    "Gub has a fetish for fucking ex-Yakuza members with big unnecessary dragon tattoos like in an old Steven Seagal flick.",
    "Gub has a 9 pack and will use it.",
    "Gub does not think of you.",
    "Gub will eventually report you for indecent exposure. Gub has seen the future and Gub knows this to be true.",
    "Gub wants to bring you on his next Louvre heist. Gub thinks you would make a good meat shield."
]

DEFAULT_GREETINGS = {
    "dankmank": "Hey master UwU",
    "APUSH": "hush you queer",
    "beans": "eat Ryan's roasted dick",
    "Ren": "go roast your dick",
    "Xx_GamerGirl42069_xX": "shush femoid",
}

NAMES = ["Mayank", "Rishabh", "Ryan", "Achint", "Lia", "Gub"]

SELF_FILE_PATH = "images/gub.png"
TEMP_QUEUED_FILE_PATH = "images/queued.png"

SHAKESPEARE_FILE_PATH = "files/shake_insults.txt"
ANIMALS_FILE_PATH = "files/animals.txt"


SAD_SIZE = file_count('images/sad/animals', 'sad')
SAD_REACT_FILE_PATHS = [f"images/sad/animals/sad{i}.jpeg" for i in range(1,SAD_SIZE+1)]

HAPPY_SIZE = file_count('images/happy/animals', 'happy')
HAPPY_REACT_FILE_PATHS = [f"images/happy/animals/happy{i}.jpeg" for i in range(1,HAPPY_SIZE+1)]

