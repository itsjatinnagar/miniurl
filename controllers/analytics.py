from controllers.database import connect


def insertAgent(lid, ua, epoch):
    query = 'INSERT INTO analytics (lid,user_agent,redirect_at) VALUES (%s, %s, %s)'
    values = (lid, ua, epoch)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def getLinkAnalytics(linkId):
    query = 'SELECT user_agent FROM analytics WHERE lid = %s'
    values = (linkId,)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query,values)

    queryResult = cursor.fetchall()

    cursor.close()
    conn.close()
    return queryResult