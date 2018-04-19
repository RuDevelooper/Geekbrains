import sqlite3

conn = sqlite3.connect('messages.db')
cursor = conn.cursor()

cursor.execute('''drop table if exists users''')
cursor.execute('''drop table if exists messages''')

cursor.execute('''
create table users(
uid integer primary key autoincrement,
login text unique )''')

cursor.execute('''
create table messages(
mid integer primary key autoincrement, 
user_from integer references users(uid),
user_to integer references users(uid),
messages text)''')

conn.commit()