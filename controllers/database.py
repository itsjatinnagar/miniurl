from urllib.parse import urlparse
import os
import psycopg2


def connect():
    URI = urlparse(os.environ['DB_URI'])
    connection = psycopg2.connect(
        host=URI.hostname,
        database=URI.path[1:],
        user=URI.username,
        password=URI.password)
    return connection


def checkHash(hash):
    query = 'SELECT * FROM links WHERE hash = %s'
    values = (hash,)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query,values)

    queryResult = cursor.fetchall()

    cursor.close()
    conn.close()
    return False if len(queryResult) == 0 else True