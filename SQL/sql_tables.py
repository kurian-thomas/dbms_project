
""" 
- Existing Tables: USER,ANS,QUES,TEST,USER_RESPONSE;
- PRAGMA used to update values of env variables. Here used to enable foreign key
  operations
- Only need to run once.

"""

import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()
c.execute("PRAGMA foreign_keys = 1")

c.execute('''CREATE TABLE USER
          (id INTEGER PRIMARY KEY,
           email text NOT NULL,
           username text NOT NULL,
           password text NOT NULL,
           type text NOT NULL)''') 



conn.commit()

c.execute('''CREATE TABLE QUES
          (id INTEGER PRIMARY KEY,
           Ques text NOT NULL)''')

conn.commit()

c.execute(''' CREATE TABLE ANS
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
           Question_id INTEGER NOT NULL,
           Ans_option text NOT NULL,
           Ans_correct text NOT NULL,
           FOREIGN KEY(Question_id) REFERENCES QUES(Qid)
           )''') 

c.execute('''CREATE TABLE TEST
          (id INTEGER PRIMARY KEY,
           Title text NOT NULL,
           Date_Time datetime default current_timestamp,
           Duration real NOT NULL)''') 

conn.commit()

c.execute('''CREATE TABLE USER_RESPONSE
          (user_id INTEGER PRIMARY KEY,
           test_id INTEGER NOT NULL,
           question_id INTEGER NOT NULL,
           answer_id INTEGER NOT NULL,
           FOREIGN KEY(user_id) REFERENCES USER(id),
           FOREIGN KEY(test_id) REFERENCES TEST(id),
           FOREIGN KEY(question_id) REFERENCES QUES(id),
           FOREIGN KEY(answer_id) REFERENCES ANS(id))''') 

conn.commit()

try:
  c.execute("DROP TABLE ADMIN")
except:
  pass

conn.commit()

c.execute('''CREATE TABLE ADMIN
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
           name text NOT NULL,
           password text NOT NULL)''') 

conn.commit() 

conn.close()