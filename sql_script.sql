-- Admin Tables Begin
DROP TABLE IF EXISTS ADMIN;
CREATE TABLE ADMIN
          (id INTEGER PRIMARY KEY AUTO_INCREMENT,
           name varchar(60) NOT NULL,
           password varchar(60) NOT NULL);
INSERT INTO ADMIN VALUES(1, 'admin', 'password');

DROP TABLE IF EXISTS TEST;
CREATE TABLE TEST
          (id INTEGER PRIMARY KEY AUTO_INCREMENT,
           title varchar(60) NOT NULL,
           description VARCHAR(100),
           date_time datetime default current_timestamp,
           duration real NOT NULL);
INSERT INTO `TEST` VALUES (1,'Data Structures','Data Structures and algorithms basics','2018-11-28 19:00:00',2);

DROP TABLE IF EXISTS QUES;
CREATE TABLE QUES
          (id INTEGER PRIMARY KEY AUTO_INCREMENT,
		   test_id INT,
           ques varchar(100) NOT NULL,
           optA VARCHAR(30),
           optB VARCHAR(30),
           optC VARCHAR(30),
           optD VARCHAR(30),
           correct VARCHAR(2));
INSERT INTO `QUES` VALUES (1,1,'Process of inserting an element to a stack is called','create','push','pop','insert','B'),(2,1,'Process of deleting an element from a stack is called','delete','remove','destroy','pop','D');
-- Admin Tables End           

CREATE TABLE USER
          (id varchar(60) PRIMARY KEY,
           email varchar(60) NOT NULL,
           username varchar(60) NOT NULL,
           password varchar(60) NOT NULL,
           type varchar(60) NOT NULL);
INSERT INTO USER VALUES('','','','','U');
INSERT INTO USER VALUES('augu','augustinetharakan12@gmail.com','augu','augu','U');

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
