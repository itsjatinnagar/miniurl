from secrets import choice
from string import ascii_letters, digits

from database.links import checkHash

def generateHash():
  CHARS = ascii_letters + digits
  while True:
    hash = ''.join(choice(CHARS) for _ in range(4))
    exists = checkHash(hash)
    if exists:
      continue
    else:
      return hash