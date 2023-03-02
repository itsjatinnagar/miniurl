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


def insertUser(email):
    conn = connect()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = 'INSERT INTO users (email) VALUES (%s) RETURNING _id'
    values = (email,)
    try:
        cursor.execute(query, values)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        logging.error(error)
        conn.close()
        return False

    userId = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return userId


def readUser(email):
    conn = connect()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = 'SELECT _id FROM users WHERE email = %s'
    values = (email,)
    try:
        cursor.execute(query, values)
    except (Exception, psycopg2.Error) as error:
        logging.error(error)
        conn.close()
        return False

    queryResult = cursor.fetchone()

    cursor.close()
    conn.close()
    return queryResult