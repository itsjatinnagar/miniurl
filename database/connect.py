from urllib.parse import urlparse
import os
import psycopg2

def connect():
    URI = urlparse(os.environ['DB_URI'])
    connection = psycopg2.connect(host=URI.hostname,database=URI.path[1:],user=URI.username,password=URI.password)
    return connection
