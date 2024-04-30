import os
import psycopg2
from psycopg2.extras import RealDictCursor

def createUser(email, created_at):
  conn = psycopg2.connect(os.environ["DB_URI"])
  query = 'INSERT INTO users (email, created_at) VALUES (%s, %s) RETURNING id'
  values = (email, created_at)
  with conn.cursor(cursor_factory=RealDictCursor) as cursor:
    cursor.execute(query, values)
    conn.commit()
    result = cursor.fetchone()
  conn.close()
  return result['id']

def readUser(email):
  conn = psycopg2.connect(os.environ["DB_URI"])
  query = 'SELECT * FROM users WHERE email = %s'
  values = (email,)
  with conn.cursor(cursor_factory=RealDictCursor) as cursor:
    cursor.execute(query, values)
    conn.commit()
    result = cursor.fetchone()
  conn.close()
  return result