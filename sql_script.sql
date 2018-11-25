
CREATE TABLE ADMIN
          (id INTEGER PRIMARY KEY AUTO_INCREMENT,
           name varchar(60) NOT NULL,
           password varchar(60) NOT NULL);
INSERT INTO ADMIN VALUES(1,'admin','password');

CREATE TABLE TEST
          (id INTEGER PRIMARY KEY,
           Title varchar(60) NOT NULL,
           Date_Time datetime default current_timestamp,
           Duration real NOT NULL);
CREATE TABLE USER
          (id varchar(11) PRIMARY KEY,
           email varchar(30) NOT NULL,
           username varchar(30) NOT NULL,
           password varchar(30) NOT NULL,
           stream varchar(5),
           sem varchar(5), 
           division varchar(5));
INSERT INTO USER VALUES('augu','augustinetharakan12@gmail.com','augu','augu','U');
CREATE TABLE QUES
          (id INTEGER PRIMARY KEY AUTO_INCREMENT,
           Ques varchar(60) NOT NULL,
           Ans_option varchar(60) NOT NULL,
           Ans_correct varchar(60) NOT NULL);
INSERT INTO QUES VALUES(1,'Choose the correct option','[]','2');
INSERT INTO QUES VALUES(2,'Choose the correct option','[''a'', ''b'', ''c'', ''d'']','2');
INSERT INTO QUES VALUES(3,'Choose the correct option','[''a'', ''b'', ''c'', ''d'']','2');
INSERT INTO QUES VALUES(4,'question','[''1'', ''2'', ''3'', ''4'']','3');
INSERT INTO QUES VALUES(5,'question','[''1'', ''2'', ''3'', ''4'']','2');
CREATE TABLE USER_RESPONSE
          (user_id INTEGER PRIMARY KEY,
           test_id INTEGER NOT NULL,
           question_id INTEGER NOT NULL);
CREATE TABLE TEST_Q(
        id INTEGER PRIMARY KEY,
        qid INTEGER NOT NULL,
        testid varchar(60) NOT NULL);

CREATE TABLE TEST_REPORT(
          user_id varchar(60) NOT NULL, 
          test_id varchar(60) NOT NULL,
          mark decimal(5,2));
COMMIT;
