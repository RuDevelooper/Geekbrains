
import sqlite3, pprint

conn = sqlite3.connect("messages.db")
cursor = conn.cursor()

cursor.execute("""
    select
        
        u1.login, u2.login, message
        
    from
    
        messages

    inner join

        users as u1

        on

            u1.uid = messages.user_from

    inner join

        users as u2

        on

            u2.uid = messages.user_to

    where

        u1.login = 'user_1'


    """)

pprint.pprint(cursor.fetchall())

