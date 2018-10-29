import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()

c.execute('''INSERT INTO ADMIN VALUES(1,"admin","password")''')

conn.commit()

conn.close()