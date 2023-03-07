from database import connect


conn = connect()
cursor = conn.cursor()

# Drop (IF)Existing Tables
cursor.execute('DROP TABLE IF EXISTS users, links')

# Create Tables
cursor.execute('CREATE TABLE users('
               '_id SERIAL,'
               'email VARCHAR(320) UNIQUE NOT NULL,'
               'PRIMARY KEY (_id)'
               ')')

cursor.execute('CREATE TABLE links('
               '_id SERIAL,'
               'uid INTEGER NOT NULL,'
               'title VARCHAR(925) NOT NULL,'
               'hash VARCHAR(16),'
               'long_url VARCHAR(2048) NOT NULL,'
               'creation_date CHAR(10) NOT NULL,'
               'click INTEGER NOT NULL DEFAULT 0,'
               'PRIMARY KEY (_id),'
               'FOREIGN KEY (uid) REFERENCES users(_id)'
               ')')

conn.commit()

cursor.close()
conn.close()
