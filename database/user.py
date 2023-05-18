from database.connect import connect

def insertUser(email):
  query = 'INSERT INTO users (email) VALUES (%s) RETURNING _id'
  values = (email,)

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