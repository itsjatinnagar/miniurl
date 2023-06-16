import os
import psycopg2

def connect():
    connection = psycopg2.connect(os.environ['DB_URI'])
    return connection
