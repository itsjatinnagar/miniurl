import logging
import psycopg2
from controllers.database import connect


def insertLink(uid,title,hash,long_url,epoch):
    conn = connect()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = 'INSERT INTO links (uid,title,hash,long_url,creation_date) VALUES (%s, %s, %s, %s, %s)'
    values = (uid, title, hash, long_url, epoch)
    try:
        cursor.execute(query, values)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        logging.error(error)
        conn.close()
        return False

    cursor.close()
    conn.close()
    return True


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