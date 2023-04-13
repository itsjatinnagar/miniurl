import logging
import random
import requests
import string
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from controllers.database import checkHash

CHARACTERS = random.sample(string.ascii_letters+string.digits, 62)

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
        response = requests.get(url, headers={"user-agent": "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36"})
        soup = BeautifulSoup(response.content, 'html.parser')
        element = soup.find('title')
        if element is None or element.string is None:
            title = urlparse(url).netloc
        else:
            title = element.string
        return title
    except requests.RequestException as error:
        logging.error(error)