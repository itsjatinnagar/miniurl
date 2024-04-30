import os
import psycopg2
from psycopg2.extras import RealDictCursor

def insertAnalytic(lid, user_agent, redirect_at):
  conn = psycopg2.connect(os.environ['DB_URI'])
  query = 'INSERT INTO analytics (lid, user_agent, redirect_at) VALUES (%s, %s, %s)'
  values = (lid, user_agent, redirect_at)
  with conn.cursor(cursor_factory=RealDictCursor) as cursor:
    cursor.execute(query, values)
    conn.commit()
  conn.close()

def readAnalytics(lid):
  conn = psycopg2.connect(os.environ['DB_URI'])
  query = 'SELECT * FROM analytics WHERE lid = %s'
  values = (lid,)
  with conn.cursor(cursor_factory=RealDictCursor) as cursor:
    cursor.execute(query, values)
    result = cursor.fetchall()
  conn.close()
  return result