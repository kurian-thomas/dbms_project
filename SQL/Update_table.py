# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:28:19 2018

@author: jishn
"""

import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()


c.execute("ALTER TABLE QUES RENAME TO quet")

c.execute("CREATE TABLE QUES (id INTEGER PRIMARY KEY,Ques text NOT NULL,Pos_marks INTEGER,Neg_marks INTEGER)")

c.execute("DROP TABLE quet")

c.execute("ALTER TABLE USER RENAME TO use")
c.execute('''CREATE TABLE USER
          (id text PRIMARY KEY,
           email text NOT NULL,
           username text NOT NULL,
           password text NOT NULL,
           type text NOT NULL)''')

c.execute("DROP TABLE use")

conn.commit()


conn.close()