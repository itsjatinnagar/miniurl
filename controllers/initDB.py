from database import connect


conn = connect()
cursor = conn.cursor()

# Drop (IF)Existing Tables
cursor.execute('DROP TABLE IF EXISTS users, links, analytics')

# Create Tables
cursor.execute('CREATE TABLE users('
               '_id SERIAL,'
               'email VARCHAR(320) UNIQUE NOT NULL,'
               'code CHAR(6),'
               'PRIMARY KEY (_id)'
               ')')

cursor.execute('CREATE TABLE links('
               '_id SERIAL,'
               'uid INTEGER NOT NULL,'
               'hash VARCHAR(16),'
               'long_url VARCHAR(2048) NOT NULL,'
               'created_at VARCHAR(10) NOT NULL,'
               'click INTEGER NOT NULL DEFAULT 0,'
               'PRIMARY KEY (_id),'
               'FOREIGN KEY (uid) REFERENCES users(_id)'
               ')')

cursor.execute('CREATE TABLE analytics('
               '_id SERIAL,'
               'lid INTEGER NOT NULL,'
               'user_agent VARCHAR(120) NOT NULL,'
               'redirect_at VARCHAR(10) NOT NULL,'
               'PRIMARY KEY (_id),'
               'FOREIGN KEY (lid) REFERENCES links(_id)'
               ')')

conn.commit()

cursor.close()
conn.close()
