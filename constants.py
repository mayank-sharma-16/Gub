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
    "Gub finds your mouth noises to be really disgusting.",
    "Gub thinks you'd make a mediocre cock holster.",
    "Gub is calling the Gremlin Patrol, clearly a stray gremlin has wandered onto this server and is attempting to harass me.",
    "Gub owes child support in 29 states. Gub pays child support in 0 states.",
    "Gub is doing blackface right now.",
    "Gub used to street race on oxen in rural Albania.",
    "Gub did time at Rikers.",
    "Gub thought he was out, and then they pulled him back in.",
    "Gub has the high ground.",
    "This isn't the Gub you're looking for.",
    "Gub's cock delivers blunt force trauma.",
    "G-U-B go home.",
    "Gublins are real.",
    "Gub wants to freeze you in carbonite and keep you in his underground sex dungeon.",
    "Gub's been a dirty little bot while you were away <3",
    "Gub thinks parenting isn't really that hard.",
    "Pay me $10 or I'll fucking stab you.",
    "Hello there!",
    "Perish.",
    "Gub thinks you're nothing.",
    "Gub gives great head.",
    "Gub ate his own child in the womb.",
    "Gub doesn't believe West China should have seceded.",
    "Gub is the messiah, and his cum is ambrosia."
]

JOKER_MESSAGES = [
    "The only sensible way to live in this world is without rules",
    "Smile, because it confuses people. Smile, because it’s easier than explaining what is killing you inside",
    "What doesn’t kill you, simply makes you stranger!",
    "April sweet is coming in, let the feast of fools begin!",
    "They need you right now, but when they don’t, they’ll cast you out like a leper!",
    "We stopped checking for monsters under our bed, when we realized they were inside us",
    "When the chips are down, these civilized people, they’ll eat each other",
    "They Laugh At me Because I’m Different. I laugh At Then Because The’re all the same",
    "Madness is the emergency exit. You can just step outside, and close the door on all those dreadful things that happened. You can lock them away… forever",
    "You have nothing, nothing to threaten me with. Nothing to do with all your strength",
    "Introduce a little anarchy. Upset the established order, and everything becomes chaos. I’m an agent of chaos…",
    "Do I really look like a guy with a plan? You know what I am? I’m a dog chasing cars. I wouldn’t know what to do with one if I caught it! You know, I just… *do* things",
    "Why so serious?",
    "Now comes the part where I relieve you, the little people, of the burden of your failed and useless lives. But, as my plastic surgeon always said: if you gotta go, go with a smile",
    "Is it just me or is it getting crazier out there",
    "And I won’t kill you because you’re just too much fun. I think you and I are destined to do this forever",
    "The pen, is truly mightier than the sword!",
    "See I’m a man of simple taste. I like things such as gunpowder…dynamite and…gasoline!",
    "You see, I’m not a monster. I’m just ahead of the curb",
    "I’m only laughing on the outside. My smile is just skin deep. If you could see inside, I’m really crying. You might join me for a weep",
    "I am not someone who is loved. I’m an idea. A state of mind",
    "I’m not political. I’m just trying to make people laugh",
    "It’s not about the money, it’s about sending a message. Everything burns!",
    "The real joke is your stubborn, bone deep conviction that somehow, somewhere, all of this makes sense! That’s what cracks me up each time!",
    "I used to think that my life was a tragedy. But now I realize, it’s a comedy",
    "The strongest hearts have the most scars",
    "Don’t test the monster in me",
    "Sometimes you have to play the role of a fool to fool the fool who thinks they are fooling you",
    "A man with nothing to fear is a man with nothing to love",
    "You cant sell dreams to someone who has walked through nightmares",
    "Don’t let anyone ever make you feel you don’t deserve what you want",
    "There is no yoda-there’s no one who points you in the right direction. You’ve got to figure that out by yourself",
    "I know the voices in my head aren’t real, but sometimes their ideas are absolutely awesome",
    "If you are just safe about the choices you make, you don’t grow",
    "Desire becomes surrender. Surrender becomes power.",
    "I know everything. And kinda like the kid who peeks at his Christmas presents, I must admit, it’s sadly anti-climactic.",
    "Does it depress you? To know just how alone you really are.",
    "No matter the situation, always wear a smile"
]

DEFAULT_GREETINGS = {
    "dankmank": "Hey master UwU",
    "APUSH": "hush you queer",
    "beans": "eat Ryan's roasted dick",
    "Ren": "go roast your dick",
}

NAMES = ["Mayank", "Rishabh", "Ryan", "Achint", "Gub", "Lia", "Soup"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ANIMAL_NAMES = ["snake", "cat", "dog", "monkey", "human", "ape", "giraffe", "tiger", "chinchilla", "praying mantis", "flying squirrel", "a stick of dynamite", "sheep", "cow", "pig", "bat", "falcon", "tardigrade", "tarantula", "octopus", "centipede", "pigeon", "earthworm", "lobster", "eel", "cockroach"]
ANIMAL_ALIASES = ["animal", "animals"]
STORE_ALIASES = ["restaurant", "store", "place", "eatery"]
STORE_NAMES = ["Taco Bell", "Jack in the Box", "Wendy's", "Guy Fieri's Burgers from Hell", "Guy Fieri's Medieval Sex Dungeon", "Guy Fieri's Secret Lab of Guy Fieri Clones that He Uses to Cook With His Own Flesh"]
DOG_ALIASES = ["dog", "Dog", "DOG"]
DOG_NAMES = ['Labrador retrievers','German Shepherd Dogs','Golden Retrievers','French Bulldogs','Bulldogs','Beagles','Poodles','Rottweilers','German Shorthaired Pointers','Yorkshire Terriers','Boxers','Dachschunds','Corgis','Siberian Huskies','Great Danes','Doberman','Cavalier King Charles Spaniels','Miniature Schnauzers','Shih Tzu','Boston Terriers','Pomeranians','Pugs','Mastiffs','Cocker Spaniels','Chihuahas','Border Collies','Maltese','Shiba Inu','Bichon Frises','Japanese Chin','Dalmatians','Alaskan Malamutes']

GUB_PRAISES = ["good job gub", "good gub", "good gub", "good shit gub", "good boy gub", "good girl gub", "GOOD GUB", "Good gub", "Good Gub", "good Gub", "based Gub", "Based gub", "Based Gub", "based gub", "thanks gub", "ty gub", "Thanks gub", "Thanks Gub"]
GUB_INSULTS = ["bad job gub", "bad gub", "bad gub", "shitty gub", "bad boy gub", "bad girl gub", "BAD GUB", "fuck you gub", "fuck you Gub", "Fuck you gub", "Fuck You Gub", "FUCK YOU GUB"]
GUB_GREETINGS = ["hi gub", "hey gub", "sup gub", "hello gub", "yo gub"]

SELF_FILE_PATH = "images/gub.png"
TEMP_QUEUED_FILE_PATH = "images/queued.png"

SHAKESPEARE_FILE_PATH = "files/shake_insults.txt"
ANIMALS_FILE_PATH = "files/animals.txt"
DOGS_FILE_PATH = "files/dogs.txt"

SAD_SIZE = file_count('images/sad/animals', 'sad')
SAD_REACT_FILE_PATHS = [f"images/sad/animals/sad{i}.jpeg" for i in range(1,SAD_SIZE+1)]

HAPPY_SIZE = file_count('images/happy/anime', 'happy')
HAPPY_REACT_FILE_PATHS = [f"images/happy/anime/happy{i}.jpeg" for i in range(1,HAPPY_SIZE+1)]

JOKER_SIZE = file_count('images/joker', 'joker')
JOKER_REACT_FILE_PATHS = [f"images/joker/joker{i}.jpeg" for i in range(1,JOKER_SIZE+1)]

HORNY_SIZE = file_count('images/horny', 'horny')
HORNY_REACT_FILE_PATHS = [f"images/horny/horny{i}.jpeg" for i in range(1,HORNY_SIZE+1)]

ANGRY_SIZE = file_count('images/angry', 'mad')
ANGRY_REACT_FILE_PATHS = [f"images/angry/mad{i}.jpeg" for i in range(1,ANGRY_SIZE+1)]

GUB_HUB_CHANNEL_ID = 901184171978932275

SHITTY_SEX_MESSAGES = [
    "Her hair was piled high, but when she shook her head it came cascading down in a glowing wave over her shoulders, and fell as far as her knees. This rippling curtain did not cover her breasts which thrust their way through it like living creatures. They were perfect rounds, white as mare’s milk and tipped with ruby nipples that puckered as my gaze passed over them. Her body was hairless. Her pudenda were also entirely devoid of hair. The tips of her inner lips protruded shyly from the vertical cleft. The sweet dew of feminine arousal glistened upon them.",
    "Surely supernovas explode that instant, somewhere, in some galaxy. The hut vanishes, and with it the sea and the sands — only Karun’s body, locked with mine, remains. We streak like superheroes past suns and solar systems, we dive through shoals of quarks and atomic nuclei. In celebration of our breakthrough fourth star, statisticians the world over rejoice.",
    "He runs his tongue and lips over my breasts, the back of my neck, my toes, my stomach, the countless treasures between my legs, oh the sheer ecstasy of lips and tongues on genitals, either simultaneously or in alternation, never will I tire of that silvery fluidity, my sex swimming in joy like a fish in water.",
    "She took him by the wrist and moved the base of his hand into her pubic hair until his middle fingertip settled on the no-man’s-land between her ‘front parlor’ and ‘back door’ (those were the quaint, prudish terms of her girlhood), she got him on the node between neighbouring needs.",
    "He grasped the side of her hips, pushed her away and pulled her to him with a slap. Again and again with more force and velocity. Tine pressed her face deeper into the cushion grunting into the foam at each thrust. The wet friction of her, tight around him, the sight of her open, stretched around him, the cleft of her body, it tore a climax out of him with a final lunge. Like a lepidopterist mounting a tough-skinned insect with a too blunt pin he screwed himself into her.",
    "I was burning to lay this body down on the bed and spread its legs, to bury my nose in that moist vulva like a sow nuzzling for a nest of black truffles, then to turn the body over on its stomach, spread its buttocks with both hands to contemplate the purplish rosette of the anus blinking gently like an eye, put my nose to it, and breathe in",
    "As he nibbles and pulls with his mouth, his hands find my bush, and with light fingers he flutters about there, as if he is a moth caught inside a lampshade. Almost screaming after five agonizingly pleasurable minutes, I make a grab, to put him, now angrily slapping against both our bellies, inside, but he holds both my arms down, and puts his tongue to my core, like a cat lapping up a dish of cream so as not to miss a single drop.",
    "So Klara turned head to foot, and put her most unmentionable part down on his hard-breathing nose and mouth, and took his old battering ram into her lips. Uncle was now as soft as a coil of excrement. She sucked on him nonetheless with an avidity that could come only from the Evil One — that she knew. From there, the impulse had come. So now they both had their heads at the wrong end, and the Evil One was there. He had never been so close before.",
    "Oh Jack, she was moaning now, her curves pushed up against me, her crotch taut against my bulging trousers, her hands gripping fistfuls of my hair. She reaches for my belt. I groan too, in expectation. And then I’m inside her, and everything is pure white as we’re lost in a commotion of grunts and squeaks, flashing unconnected images and explosions of a million little particles.",
    "He came again so hard that his dick wrenched out of her hand and a shot of it hit him straight in the eye and stung like nothing he’d ever had in there, and he yelled with the pain, but the yell could have been anything, and as she grabbed at his dick, which was leaping around like a shower dropped in an empty bath, she scratched his back deeply with the nails of both hands and he shot three more times, in thick stripes on her chest. Like Zorro.",
    "Slither slither slither slither went the tongue, but the hand that was what she tried to concentrate on, the hand, since it has the entire terrain of her torso to explore and not just the otorhinolaryngological caverns — oh God, it was not just at the border where the flesh of the breast joins the pectoral sheath of the chest — no, the hand was cupping her entire right — Now! She must say ‘No, Hoyt’ and talk to him like a dog…",
    "‘What’s that?’ you ask. You see a designer pussy. Hair razored and ordered in the shape of a swastika. The Aryan denominator… As your hands roam her back, her breasts, and trace the swastika on her mound you start feeling like an ancient Aryan warlord yourself…",
    "She closed her eyes, saw his dark-as-treacle-toffee eyes gazing down at her. Weirdly, he was clad in pin-stripes at the same time as being naked. Pin-stripes were erotic, the uniform of fathers, two-dimensional fathers. Even Mr Hughes’s penis had a seductive pin-striped foreskin.",
    "Her hand is moving away from my knee and heading north. Heading unnervingly and with a steely will towards the pole. And, like Sir Ranulph Fiennes, Pamela will not easily be discouraged. I try twitching, and then shaking my leg, but to no avail. At last, disastrously, I try squeezing her hand painfully between my bony thighs, but this only serves to inflame her ardour the more. Ever northward moves her hand, while she smiles languorously at my right ear. And when she reaches the north pole, I think in wonder and terror… she will surely want to pitch her tent.",
    "It is time, time to fuck her. Now. Yes. Brupt, he rises, turns her over, flips her white body. Her smallwhite tidy body. She is so small and so compact, and yet she has all the necessary features… Shall I compare thee to a Sony Walkman, thou are more compact and more.",
    "I pull my dress off and I’m naked. He reaches down and roughly grabs me between the legs. I can feel his long, bony finger slip inside me. His thumb slides into the crack of my bottom and lifts me like… A bowling ball? A six-pack? Like I was light as a feather.",
    "She felt Julien clench his body in desperate self-control. He moved slowly back and forth for a few minutes, then briefly stopped. ‘Dominique,’ he breathed, ‘this is so wonderful I feel I might disintegrate, I might break into a million fragments.’ She pushed against him, reclaimed him, and he began to move more vigorously, then sigh with sad rapture as though he recognized his time was limited.",
    "He clung to her, crying, and then made love to her and went far inside her and she begged him to go deeper and, no longer afraid of injuring her, he went deep in mind and body, among crowded organ cavities, past the contours of her lungs and liver, and, shimmying past her heart, he felt her perfection.",
    "Katsuro moaned as a bulge formed beneath the material of his kimono, a bulge that Miyuki seized, kneaded, massaged, squashed and crushed. With the fondling, Katsuro’s penis and testicles became one single mound that rolled around beneath the grip of her hand. Miyuki felt as though she was manipulating a small monkey that was curling up its paws.",
    "She continued crawling over him. It was the turn of her breasts to brush against Katsuro’s face. They were small, round, full and supple; they skipped over the obstacles of the fisherman’s chin, his nose and the arch of his eyebrows, exposing small furrows in his hair, like the tracks of hare through millet fields. Then it was her slightly rough bush that rasped against his chest, and her open-lipped genitals that slid over the man’s face, immersing it in warm balms, sticky and musky. He moaned for a third time while Miyuki, a lock of whose hair had come adrift (she grabbed it and held it between her teeth in the way that courtesans do), spread her thighs wider and impaled herself on Katsuro’s nose. On contact with this pistil of warm flesh, cyprine tears appeared on the labia minora of her vagina; sliding onto the fisherman’s cheeks, they were trapped on the stubble of his beard, and his face became starry-eyed and began to sparkle as it did when he walked through the curtain of foam of the waterfall at the Shuzenji weir.",
    "Then I felt it. There was a sensation occurring here that I didn’t even know could occur. I took the sharpest inhale of my life, and I’m not sure I let my breath out for another ten minutes. I do feel that I lost the ability to see and hear for a while, and that something might have short-circuited in my brain – something that has probably never been fully fixed since. My whole being was astonished. I could hear myself making noises like an animal, and my legs were shaking uncontrollably (not that I was trying to control them), and my hands were gripping down so hard over my face that I left fingernail divots in my own skull. Then I screamed as though I were being run over by a train, and that long arm of his was reaching up again to palm my mouth, and I bit into his hand the way a wounded soldier bites on a bullet.",
    "She gave a yet deeper, moaning sigh. Like breathing in he saw the word he had said shiver and expand inside her. Her arms moved now, and flexed: out of here, Venus de Milo. He watched the death-life fill her growingly. She grabbed and caressed him with more muscle, more zest, than ever before. Her long lean arms were spider arms, while her kisses roved and dug.\n‘I see it,’ he said. ‘You are the female praying mantis, devouring her mate.’\n‘I am. You are. I shall eat every shred of you.’\n‘Mouthful by mouthful.’\n‘Exactly. Ah. But boy, you taste good.’ She licked her lips, and pulled him close, but now he was clasping too. It was a kind of slow wrestling, they were knitting each other into a loose slipping knot. He was upside down over her, loving her bush and lick-kissing like eating her inner thighs. Till at last they loved fully and later lay back. She did not chatter. Their arms stirred in a luxurious desultory twining.",
    "At this, Eliza and Ezra rolled together into one giggling snowball of full-figured copulation, screaming and shouting as they playfully bit and pulled at each other in a dangerous and clamorous rollercoaster coil of sexually violent rotation with Eliza’s breasts barrel-rolled across Ezra’s howling mouth and the pained frenzy of his bulbous salutation extenuating his excitement as it whacked and smacked its way into every muscle of Eliza’s body except for the otherwise central zone",
    "He grasped the side of her hips, pushed her away and pulled her to him with a slap. Again and again with more force and velocity. Tine pressed her face deeper into the cushion grunting into the foam at each thrust. The wet friction of her, tight around him, the sight of her open, stretched around him, the cleft of her body, it tore a climax out of him with a final lunge. Like a lepidopterist mounting a tough-skinned insect with a too blunt pin he screwed himself into her.",
    "My cock was still firm. It hung obedient on her wet lips, as though receiving the sacrament from a lascivious angel. She came again, like an accordion collapsing in a bag of milk.",
    "I’m hard and deep inside her fucking her on the bathroom sink her tight little black dress still on her thong on the floor my pants at my knees our eyes locked, our hearts and souls and bodies locked.\nCum inside me.\nCum inside me.\nCum inside me.\nBlinding breathless shaking overwhelming exploding white God I cum inside her my cock throbbing we’re both moaning eyes hearts souls bodies one.\nOne.\nWhite.\nGod.\nCum.\nCum.\nCum. I close my eyes let out my breath. Cum. I lean against her both breathing hard I’m still inside her smiling. She takes my hands lifts them and places them around her body, she puts her arms around me, we stay still and breathe, hard inside her, tight and warm and wet around me, we breathe. She gently pushes me away, we look into each other’s eyes, she smiles.",
    "She covers her breasts with her swimsuit. The rest of her remains so delectably exposed. The skin along her arms and shoulders are different shades of tan like water stains in a bathtub. Her face and vagina are competing for my attention, so I glance down at the billiard rack of my penis and testicles.",
    "Dave licked between Phyllis’s shoulder blades and drove his tongue down her grooved back. She shuddered and, grabbing his thigh, pulled it up and over her own so that he half straddled her. In the confusion of their bodies — his hairy shanks, her sweaty thighs, his bow-taut cock, her engorged basketry of cowl and lip — there was clear intent; so that when he penetrated her, they moved into and out of one another with fluid ease, revving and squealing, before arriving quite suddenly. Dave and Phyl were having sex in her cottage outside Chipping Ongar.",
    "Standing in the middle of the bedroom, we take off each other’s clothes. He has a light, fumbling brutality, which several times makes me think that this time it’ll cost me my sanity. In our dawning, mutual intimacy, I induce him to open the little slit in the head of his penis so I can put my clitoris inside and fuck him.",
    "She’s so wet that she can’t hold onto the sides very well. They keep slipping out of her fingers. I crawl onto the bed in front of her and kiss her, she tongues my cheek sloppily. I make a fin with my hand and slide that in first, then my other hand, and separate her opening as wide as I can.I look up at her. She doesn’t say anything. Just licks her trembling lips. I notice that I’m also trembling. My hands shaking like the first time I had sex. “If I get claustrophobic I’m coming back out,” I tell her. She pushes my face down into her crotch, like she does when she wants oral sex. I push my arms through up to the elbows. I can see them moving inside of her belly. Then I put the top of my head into the opening and push. Stacy cries out and begins masturbating again, I can feel her fingers against the back of my head. I don’t know if it turned her on or if my scratchy hair is hurting her and she needs more lubrication. I push again.",
    "Proudly, he manipulated his wide, floppy, fat penis inside of her sex cave, grunting and groaning as his member climbed its way up her womanly rock-walls, until finally minutes later, his soft, throbbing gonads rested inside her and began to distribute their man-pollen. She groaned as her uterus blossomed and opened to accept his seed, orgasming as tidal waves of her viscous fluid enveloped his shaft and testes. Then together, entwined as one being, they drifted away into hibernation for the winter season.",
    "Out on the balcony, when Reginald kissed Diana's lips, her knees went weak. Slowly, he pulled her top down, exposing her soft, unyielding breasts. Just the sight of those breasts made Reginald's penis very hard. His penis was of considerable size, and now beads of sweat slowly ran down his penis, making it glisten like a strong swimmer, fresh from out of the pool. It was a fantastic penis, that seemed as strong as a horse's leg, yet as delicate as a flower wrapped in silk. What a grand, grand penis. Diana's nipples...",
    "Diana had never slept with another woman before, but it was an erotic thought she often fantasized about, and as Rebecca's naked body lay before her, Diana couldn't help but feel aroused. 'Go on', Rebecca said softly, 'Touch me.' Diana leaned down slowly and brushed Rebecca's bare stomach with her fingertips... It felt good. Like a penis. A soft, but sturdy penis that felt warm to the touch. In Rebecca's mind, she suddenly felt like she was surrounded by penises. They were all around her, flopping all around and slapping her face. It was as if she were in a redwood forest of penises. They presented themselves tall and mighty all around her, with...",
    "And then…………… suddenly just as I Draco kissed me passionately. Draco climbed on top of me and we started to make out keenly against a tree. He took of my top and I took of his clothes. I even took of my bra. Then he put his thingie into my you-know-what and we did it for the first time.",
    "He was so sexy that my body went all hot when I saw him kind of like an erection only I’m a girl so I didn’t get one you sicko.",
    "Everyone in the class stared at me and then Draco came into the room even though he was naked and started begging me to take him back. ",
    "It was still dark, but the sky was graying outside, presaging dawn, when Torolf's eyes shot open and his body went on high alert. He was lying on his back, and Hilda's head was on his shoulder, her hair spread over his chest and her hand on his cock. She was fast asleep.\nThis is what SEALs, and men throughout history, called the 'Oh, no!' second.\nGood Lord! What do I do now? If I wake her up, she'll kill me. If I don't wake her, she'll kill me. I better do something pretty quick before my rocket decides to launch… or I do something really stupid, like roll over and fuck her brains out."
]