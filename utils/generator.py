from secrets import choice
from string import ascii_letters, digits
from controllers.link_controller import LinkController

def generateHash():
    CHARS = ascii_letters + digits
    while True:
        hash = ''.join(choice(CHARS) for _ in range(4))
        exists = LinkController.get_link(hash)
        if exists:
            continue
        else:
            return hash