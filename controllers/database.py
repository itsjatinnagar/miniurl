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

def insertLink(uid,title,long_url,epoch):
    conn = connect()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = 'INSERT INTO links (uid,title,long_url,creation_date) VALUES (%s, %s, %s, %s) RETURNING _id'
    values = (uid, title, long_url, epoch,)
    try:
        cursor.execute(query, values)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        logging.error(error)
        conn.close()
        return False

    linkId = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return linkId

def updateLink(id, data):
    conn = connect()
    if conn is None:
        return False
    
    cursor = conn.cursor()
    query = 'UPDATE links SET {} = %s WHERE _id = {}'.format(', '.join(data.keys()), id)
    values = tuple(data.values())
    try:
        cursor.execute(query,values)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        logging.error(error)
        conn.close()
        return False

    cursor.close()
    conn.close()
    return True

def getLinks(userId):
    conn = connect()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = 'SELECT _id,long_url,hash FROM links WHERE uid = %s ORDER BY creation_date DESC'
    values = (userId,)
    try:
        cursor.execute(query,values)
    except (Exception, psycopg2.Error) as error:
        logging.error(error)
        conn.close()
        return False

    queryResult = cursor.fetchall()

    cursor.close()
    conn.close()
    return queryResult

def readLink(linkId):
    conn = connect()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = 'SELECT * FROM links WHERE _id = %s'
    values = (linkId,)
    try:
        cursor.execute(query,values)
    except (Exception, psycopg2.Error) as error:
        logging.error(error)
        conn.close()
        return False

    queryResult = cursor.fetchone()

    cursor.close()
    conn.close()
    return queryResult

def readLongLink(hash):
    conn = connect()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = 'SELECT long_url FROM links WHERE hash = %s'
    values = (hash,)
    try:
        cursor.execute(query,values)
    except (Exception, psycopg2.Error) as error:
        logging.error(error)
        conn.close()
        return False

    queryResult = cursor.fetchone()

    cursor.close()
    conn.close()
    return queryResult