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
        if response.status_code == 200:
            html = response.text
            return html[html.find('<title>')+7 : html.find('</title>')]
        else:
            return url[8:]
    except requests.RequestException as error:
        logging.error(error)