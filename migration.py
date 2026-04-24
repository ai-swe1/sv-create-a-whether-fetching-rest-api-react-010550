import sqlite3
connection = sqlite3.connect('weather.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS weather (id INTEGER PRIMARY KEY, temperature REAL, humidity REAL);')
connection.close()