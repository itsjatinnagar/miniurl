from bs4 import BeautifulSoup
import logging
import requests
import string

ELEMENTS = string.ascii_letters+string.digits[1:]

def generateHash(num):
    hash = str()
    while num != 0:
        hash += ELEMENTS[num%len(ELEMENTS)]
        num //= len(ELEMENTS)
    while len(hash) != 4:
        hash += '0'
    return hash

def fetchTitle(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.title.string
    except requests.RequestException as error:
        logging.error(error)