from database.connect import connect

def insertAgent(lid, user_agent, redirect_at):
    query = 'INSERT INTO analytics (lid, user_agent, redirect_at) VALUES (%s, %s, %s)'
    values = (lid,user_agent,redirect_at)

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query,values)
    conn.commit()

    cursor.close()
    conn.close()