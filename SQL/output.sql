PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE TEST
          (id INTEGER PRIMARY KEY,
           Title text NOT NULL,
           Date_Time datetime default current_timestamp,
           Duration real NOT NULL);
CREATE TABLE ADMIN
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
           name text NOT NULL,
           password text NOT NULL);
INSERT INTO ADMIN VALUES(1,'admin','password');
CREATE TABLE USER
          (id text PRIMARY KEY,
           email text NOT NULL,
           username text NOT NULL,
           password text NOT NULL,
           type text NOT NULL);
INSERT INTO USER VALUES('','','','','U');
INSERT INTO USER VALUES('augu','augustinetharakan12@gmail.com','augu','augu','U');
CREATE TABLE QUES
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
           Ques text NOT NULL,
           Ans_option text NOT NULL,
           Ans_correct text NOT NULL);
INSERT INTO QUES VALUES(1,'Choose the correct option','[]','2');
INSERT INTO QUES VALUES(2,'Choose the correct option','[''a'', ''b'', ''c'', ''d'']','2');
INSERT INTO QUES VALUES(3,'Choose the correct option','[''a'', ''b'', ''c'', ''d'']','2');
INSERT INTO QUES VALUES(4,'question','[''1'', ''2'', ''3'', ''4'']','3');
INSERT INTO QUES VALUES(5,'question','[''1'', ''2'', ''3'', ''4'']','2');
CREATE TABLE USER_RESPONSE
          (user_id INTEGER PRIMARY KEY,
           test_id INTEGER NOT NULL,
           question_id INTEGER NOT NULL,
           FOREIGN KEY(user_id) REFERENCES USER(id),
           FOREIGN KEY(test_id) REFERENCES TEST(id),
           FOREIGN KEY(question_id) REFERENCES QUES(id));
CREATE TABLE TEST_Q(
        id INTEGER PRIMARY KEY,
        qid INTEGER NOT NULL,
        testid text NOT NULL,
        FOREIGN KEY(qid) REFERENCES QUES(id),
        FOREIGN KEY(testid) REFERENCES TEST(test_id));
CREATE TABLE TEST_REPORT(
          user_id text NOT NULL, 
          test_id text NOT NULL,
          mark decimal(5,2),
          FOREIGN KEY(user_id) REFERENCES USER(id),
          FOREIGN KEY(test_id) REFERENCES TEST(test_id));
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('ADMIN',1);
INSERT INTO sqlite_sequence VALUES('QUES',5);
COMMIT;
