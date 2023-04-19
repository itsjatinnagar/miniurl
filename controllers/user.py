from controllers.database import connect


def insertUser(email, code):
    query = 'INSERT INTO users (email,code) VALUES (%s,%s) RETURNING _id'
    values = (email, code)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()

    userId = cursor.fetchone()[0]

    cursor.close()
    conn.close()
    return userId


def updateUser(id, code):
    query = 'UPDATE users SET code = %s WHERE _id = %s'
    values = (code, id)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def readUserWithMail(email):
    query = 'SELECT * FROM users WHERE email = %s'
    values = (email,)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, values)

    queryResult = cursor.fetchone()

    cursor.close()
    conn.close()
    return queryResult


def readUserWithId(id):
    query = 'SELECT * FROM users WHERE _id = %s'
    values = (id,)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, values)
    
    queryResult = cursor.fetchone()

    cursor.close()
    conn.close()
    return queryResult
