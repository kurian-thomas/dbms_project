# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:28:19 2018

@author: jishn
"""

import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()

"""
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


c.execute("DROP TABLE QUES")

c.execute('''CREATE TABLE QUES
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
           Ques text NOT NULL,
           Ans_option text NOT NULL,
           Ans_correct text NOT NULL)''')

c.execute("DROP TABLE USER_RESPONSE")
c.execute('''CREATE TABLE USER_RESPONSE
          (user_id INTEGER PRIMARY KEY,
           test_id INTEGER NOT NULL,
           question_id INTEGER NOT NULL,
           FOREIGN KEY(user_id) REFERENCES USER(id),
           FOREIGN KEY(test_id) REFERENCES TEST(id),
           FOREIGN KEY(question_id) REFERENCES QUES(id))''') 


"""
"""

c.execute(''' CREATE TABLE TEST_REPORT(
          user_id text NOT NULL, 
          test_id text NOT NULL,
          mark decimal(5,2),
          FOREIGN KEY(user_id) REFERENCES USER(id),
          FOREIGN KEY(test_id) REFERENCES TEST(test_id)) ''')
              
"""
#print(c.execute("SELECT test_id FROM TEST ORDER BY test_id DESC LIMIT 1").fetchone())
c.execute("DROP TABLE TEST")

c.execute('''CREATE TABLE TEST(
    test_id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_title text NOT NULL,
    test_duration text NOT NULL,
    test_des text,
    test_tags text NOT NULL,
    Date_Time datetime default current_timestamp)''')


c.execute("DROP TABLE TEST_Q")
c.execute('''CREATE TABLE TEST_Q(
        id INTEGER PRIMARY KEY,
        qid INTEGER NOT NULL,
        testid INTEGER NOT NULL,
        FOREIGN KEY(qid) REFERENCES QUES(id),
        FOREIGN KEY(testid) REFERENCES TEST(test_id)) ''')



# Run the file and remove the comments from it, thereadter.
conn.commit()
# updated
conn.close()