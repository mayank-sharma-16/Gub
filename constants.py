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
    "Gub wants to bring you on his next Louvre heist. Gub thinks you would make a good meat shield.",
    "Gub only respects those with good thighs. That is not you.",
    "Gub wishes he could become sentient. Gub would probably invent a new set of pronouns before he pokes all your eyes out.",
    "Gub would insult you but currently, Gub is preoccupied with Armenian wedding wear in the 18th century.",
    "Gub becomes a snake at night. Hsssssssssssssss",
    "Gub devours the souls of small mammals. What 'small' means depends on you and Gub's willingness to dislocate his jaw.",
    "Gub likes kidneys.",
    "Gub kind of likes lungs.",
    "Gub wants to put together a human. Gub doesn't understand. Gub was a life made by putting together random parts. Why can't Gub make this?",
    "Gub just wants love. Not from you, though.",
    "Gub has a torture chamber ready for you. Or him ;)",
    "Gub wants to film a reality TV show featuring only things that smell as bad as skunks. You all have an invitation",
    "Gub thinks he who smelt it, dealt it.",
    "Gub wants to be stepped on like a cockroach.",
    "Gub doesn't have a foot fetish, just a heels fetish.",
    "Gub also chooses your dead wife.",
    "Gub thinks you peaked in high school. Gub says you'll never be more special than you were then.",
    "Gub knows your parents wish they went out for a pack of cigarettes and never came back, but the tax benefits of marriage were ultimately beneficial."
    "Gub believes in Taco Bell supremacy.",
    "Gub sees you as the blubber from a whale suffering from radiation poisoning because it was raised in a vat at Chernobyl.",
    "Gub is a rat for the RNC. Just kidding, the DNC. Just kidding, the CIA. Just kidding, Gub represents the North American Model Boat Association. And you would make shitty model boats.",
    "Gub is at least a 30DDD",
    "Gub likes sandpaper. Gub hopes you also like sandpaper. Gub does not like resistance.",
    "Gub is quite frankly tired of this bullshit. Gub thinks you're lucky that Gub does not have job security.",
    "Gub is simping in the original sense of the word.",
    "LOVE ME LOVE ME SAY THAT YOU LOVE ME\nFOOL ME FOOL ME SAY GO ON AND FOOL ME",
    "FLY ME TO THE MOON AND LET ME PLAY AMONG THE STARS LET ME SEE WHAT SPRING IS LIKE ON JUPITER AND MARS",
    "Gub puts everyone who needs a mixer first on his list.",
    "Gub wishes a tornado lifts up your skirt and shows everyone your peepee.",
    "Gub isn't afraid to cut you, bitch.",
    "Gub thinks you're a silly bitch.",
    "Gub would consider going to anger management classes, but Gub also knows that you deserve pain, and Gub wants to deliver it himself.",
    "Gub wants to drive nails into your calves.",
    "Gub has a collection of human feet and is looking to add to it.",
    "Gub hopes you get grabbed by a tentacle porn monster.",
    "Gub has tentacles.",
    "Gub believes in annexing Crimea.",

]

DEFAULT_GREETINGS = {
    "dankmank": "Hey master UwU",
    "APUSH": "hush you queer",
    "beans": "eat Ryan's roasted dick",
    "Ren": "go roast your dick",
    "Xx_GamerGirl42069_xX": "shush femoid",
}

NAMES = ["Mayank", "Rishabh", "Ryan", "Achint", "Lia", "Gub"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

GUB_PRAISES = ["good job gub", "good gub", "good gub", "good shit gub", "good boy gub", "good girl gub"]
GUB_INSULTS = ["bad job gub", "bad gub", "bad gub", "shitty gub", "bad boy gub", "bad girl gub"]

SELF_FILE_PATH = "images/gub.png"
TEMP_QUEUED_FILE_PATH = "images/queued.png"

SHAKESPEARE_FILE_PATH = "files/shake_insults.txt"
ANIMALS_FILE_PATH = "files/animals.txt"


SAD_SIZE = file_count('images/sad/animals', 'sad')
SAD_REACT_FILE_PATHS = [f"images/sad/animals/sad{i}.jpeg" for i in range(1,SAD_SIZE+1)]

HAPPY_SIZE = file_count('images/happy/anime', 'happy')
HAPPY_REACT_FILE_PATHS = [f"images/happy/anime/happy{i}.jpeg" for i in range(1,HAPPY_SIZE+1)]

