from database.connect import connect

def insertUser(email,created_at):
  query = 'INSERT INTO users (email,created_at) VALUES (%s,%s) RETURNING _id'
  values = (email,created_at)

  conn = connect()
  cursor = conn.cursor()

  cursor.execute(query, values)
  conn.commit()

  userId = cursor.fetchone()[0]

  cursor.close()
  conn.close()
  return userId

def readUser(email):
  query = 'SELECT * FROM users WHERE email = %s'
  values = (email,)

  conn = connect()
  cursor = conn.cursor()
  cursor.execute(query, values)

  queryResult = cursor.fetchone()

  cursor.close()
  conn.close()
  return queryResult