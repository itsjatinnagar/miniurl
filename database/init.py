import os
import psycopg2

connection = psycopg2.connect(os.environ['DB_URI'])
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS users, links, analytics')

cursor.execute('CREATE TABLE users('
               'id INTEGER GENERATED ALWAYS AS IDENTITY,'
               'email VARCHAR(320) UNIQUE NOT NULL,'
               'created_at VARCHAR(10) NOT NULL,'
               'PRIMARY KEY (id))')

cursor.execute('CREATE TABLE links('
               'id INTEGER GENERATED ALWAYS AS IDENTITY,'
               'uid INTEGER NOT NULL,'
               'hash CHAR(4) UNIQUE NOT NULL,'
               'long_url VARCHAR(2048) NOT NULL,'
               'created_at VARCHAR(10) NOT NULL,'
               'clicks INTEGER NOT NULL DEFAULT 0,'
               'PRIMARY KEY (id),'
               'FOREIGN KEY (uid) REFERENCES users(id))')

cursor.execute('CREATE TABLE analytics('
               'id INTEGER GENERATED ALWAYS AS IDENTITY,'
               'lid INTEGER NOT NULL,'
               'user_agent VARCHAR(180) NOT NULL,'
               'redirect_at VARCHAR(10) NOT NULL,'
               'PRIMARY KEY (id),'
               'FOREIGN KEY (lid) REFERENCES links(id))')

connection.commit()
cursor.close()
connection.close()