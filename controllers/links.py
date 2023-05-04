from controllers.database import connect


def insertLink(uid,hash,long_url,epoch):
    query = 'INSERT INTO links (uid,hash,long_url,created_at) VALUES (%s, %s, %s, %s)'
    values = (uid, hash, long_url, epoch)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def updateLink(id, data):
    query = 'UPDATE links SET {} = %s WHERE _id = {}'.format(', '.join(data.keys()), id)
    values = tuple(data.values())

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()


def getLinks(userId):
    query = 'SELECT * FROM links WHERE uid = %s ORDER BY created_at DESC'
    values = (userId,)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query,values)

    queryResult = cursor.fetchall()

    cursor.close()
    conn.close()
    return queryResult


def readLink(linkId):
    query = 'SELECT * FROM links WHERE _id = %s'
    values = (linkId,)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query,values)

    queryResult = cursor.fetchone()

    cursor.close()
    conn.close()
    return queryResult


def readLongLink(hash):
    query = 'SELECT _id,long_url,click FROM links WHERE hash = %s'
    values = (hash,)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query,values)

    queryResult = cursor.fetchone()

    cursor.close()
    conn.close()
    return queryResult