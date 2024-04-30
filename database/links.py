import os
import psycopg2
from psycopg2.extras import RealDictCursor

def createLink(uid, hash, long_url, created_at):
  conn = psycopg2.connect(os.environ['DB_URI'])
  query = 'INSERT INTO links (uid, hash, long_url, created_at) VALUES (%s, %s, %s, %s) RETURNING id'
  values = (uid, hash, long_url, created_at)
  with conn.cursor(cursor_factory=RealDictCursor) as cursor:
    cursor.execute(query, values)
    conn.commit()
    result = cursor.fetchone()
  conn.close()
  return result['id']

def readLinks(uid):
  conn = psycopg2.connect(os.environ['DB_URI'])
  query = 'SELECT * FROM links WHERE uid = %s ORDER BY created_at DESC'
  values = (uid,)
  with conn.cursor(cursor_factory=RealDictCursor) as cursor:
    cursor.execute(query, values)
    result = cursor.fetchall()
  conn.close()
  return result

def updateLink(id, clicks):
  conn = psycopg2.connect(os.environ['DB_URI'])
  query = 'UPDATE links SET clicks = %s WHERE id = %s'
  values = (clicks, id)
  with conn.cursor(cursor_factory=RealDictCursor) as cursor:
    cursor.execute(query, values)
    conn.commit()
  conn.close()

def readLongLink(hash):
  conn = psycopg2.connect(os.environ['DB_URI'])
  query = 'SELECT id, long_url, clicks FROM links WHERE hash = %s'
  values = (hash,)
  with conn.cursor(cursor_factory=RealDictCursor) as cursor:
    cursor.execute(query, values)
    result = cursor.fetchone()
  conn.close()
  return result

def checkHash(hash):
  conn = psycopg2.connect(os.environ['DB_URI'])
  query = 'SELECT id FROM links WHERE hash = %s'
  values = (hash,)
  with conn.cursor(cursor_factory=RealDictCursor) as cursor:
    cursor.execute(query, values)
    result = cursor.fetchall()
  conn.close()
  return True if len(result) else False