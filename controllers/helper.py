import random
from bs4 import BeautifulSoup
import logging
import requests
import string

from controllers.database import checkHash

CHARACTERS = string.ascii_letters + string.digits

def generateHash(num):
    while True:
        hash = ''.join(random.choices(CHARACTERS,k=num))
        isPresent = checkHash(hash)
        if isPresent:
            break
        elif isPresent is None:
            return False
    return hash


def fetchTitle(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.title.string
    except requests.RequestException as error:
        logging.error(error)