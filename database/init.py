from urllib.parse import urlparse
import os
import psycopg2

URI = urlparse(os.environ['DB_URI'])
connection = psycopg2.connect(host=URI.hostname,database=URI.path[1:],user=URI.username,password=URI.password)

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS users, links, analytics')

cursor.execute('CREATE TABLE users('
            '_id SERIAL,'
            'email VARCHAR(320) UNIQUE NOT NULL,'
            'PRIMARY KEY (_id)'
            ')')

cursor.execute('CREATE TABLE links('
            '_id SERIAL,'
            'uid INTEGER NOT NULL,'
            'hash VARCHAR(4),'
            'long_url VARCHAR(2048) NOT NULL,'
            'created_at VARCHAR(10) NOT NULL,'
            'clicks INTEGER NOT NULL DEFAULT 0,'
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

connection.commit()
cursor.close()
connection.close()
