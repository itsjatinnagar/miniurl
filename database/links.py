from database.connect import connect

def insertLink(userId, hash, longLink, created_at):
    query = 'INSERT INTO links (uid,hash,long_url,created_at) VALUES (%s,%s,%s,%s) RETURNING _id'
    values = (userId,hash,longLink,created_at)

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query,values)
    conn.commit()

    linkId = cursor.fetchone()[0]

    cursor.close()
    conn.close()
    return linkId

def updateLinkClicks(id,clicks):
    query = "UPDATE links SET clicks = %s WHERE _id = %s"
    values = (clicks,id)

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query,values)
    conn.commit()

    cursor.close()
    conn.close()

def readAllLinks(userId):
    query = 'SELECT * FROM links WHERE uid = %s ORDER BY created_at DESC'
    values= (userId,)

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query,values)
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result

def readRedirectLink(hash):
    query = 'SELECT _id,long_url,clicks FROM links WHERE hash = %s'
    values = (hash,)

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query,values)
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result

def hashExists(hash):
    query = 'SELECT _id FROM links WHERE hash = %s'
    values = (hash,)

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query,values)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return True if len(result) else False