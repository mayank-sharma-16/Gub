from orders import orders as commands
from constants import GUB_PRAISES, GUB_INSULTS


def gub_mentioned(message):
    
    if len(message.content) > 0 and message.content[:3].lower() == "gub":
        return True
    return False


def gub_commanded(message):

    if len(message.content.split()) > 1:
        return True
    return False


def gubs_messaged(message):

    if message.author.name.lower() == "gub":
        return True
    return False


def gub_praised(message):

    message_content = message.content.lower()
    if message_content in GUB_PRAISES:
        return 1
    elif message_content in GUB_INSULTS:
        return 2
    else:
        return 0


def check_command(message):

    if not gub_commanded(message):
        return None

    message_command = message.content.split(' ')[1]
    for command in commands.values():
        if message_command in command.aliases:
            return command.name

    return None



