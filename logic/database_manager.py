import sqlite3

conn = sqlite3.connect('../data/history.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS unfollowers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        date_lost DATETIME DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(username, date_lost)
        )
''')

conn.commit()
conn.close()