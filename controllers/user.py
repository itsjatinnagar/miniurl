import logging
import psycopg2
from controllers.database import connect


def insertUser(email, code):
    conn = connect()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = 'INSERT INTO users (email,code) VALUES (%s,%s) RETURNING _id'
    values = (email, code)
    try:
        cursor.execute(query, values)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        logging.error(error)
        conn.close()
        return False

    userId = cursor.fetchone()
    cursor.close()
    conn.close()
    return userId


def updateUser(id, code):
    conn = connect()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = 'UPDATE users SET code = %s WHERE _id = %s'
    values = (code, id)
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


def readUserWithMail(email):
    conn = connect()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = 'SELECT * FROM users WHERE email = %s'
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


def readUserWithId(id):
    conn = connect()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = 'SELECT * FROM users WHERE _id = %s'
    values = (id,)
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
