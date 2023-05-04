import random
import string

from controllers.database import checkHash

CHARACTERS = random.sample(string.ascii_letters+string.digits, 62)

def generateHash(num):
    while True:
        hash = ''.join(random.choices(CHARACTERS,k=num))
        isPresent = checkHash(hash)
        if isPresent:
            continue
        else:
            break
    return hash


def generateCode(length):
    return ''.join(random.choices(string.digits, k=length))