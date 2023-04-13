from urllib.parse import urlparse
import logging
import os
import psycopg2


def connect():
    URI = urlparse(os.environ['DB_URI'])
    try:
        connection = psycopg2.connect(
            host=URI.hostname,
            database=URI.path[1:],
            user=URI.username,
            password=URI.password)
        return connection
    except (Exception, psycopg2.Error) as error:
        logging.error(error)


def checkHash(hash):
    conn = connect()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = 'SELECT * FROM links WHERE hash = %s'
    values = (hash,)
    try:
        cursor.execute(query,values)
    except (Exception, psycopg2.Error) as error: 
        logging.error(error)
        conn.close()
        return False

    queryResult = cursor.fetchall()

    cursor.close()
    conn.close()
    return True if len(queryResult) == 0 else None