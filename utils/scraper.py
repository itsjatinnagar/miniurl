import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def extract_title(url):
    domain = urlparse(url).netloc
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.find_all('title')
    if not len(titles):
        return domain
    return titles[-1].text