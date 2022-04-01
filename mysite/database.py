import sqlite3

#Open database
conn = sqlite3.connect('/home/gshkr/database.db')


conn.execute('''CREATE TABLE programs
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        genre TEXT,
        network TEXT,
        viewer_city TEXT,
        viewers_count INTEGER
		)''')

conn.close()

