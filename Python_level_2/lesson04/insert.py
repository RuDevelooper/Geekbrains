import sqlite3

conn = sqlite3.connect('messages.db')
cursor = conn.cursor()

cursor.execute('''
insert
into users
(login)
values
('user_1'), ('user_2'), ('user_3')''')

conn.commit()

cursor.execute('''
insert into messages
(user_from, user_to, messages)
values
(1, 2, 'Hello from 1 to 2'),
(1, 3, 'Hello from 1 to 2'),
(3, 2, 'Hello from 1 to 2'),
(1, 1, 'Hello from 1 to 2')''')