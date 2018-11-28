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
           ques varchar(200) NOT NULL,
           optA VARCHAR(50),
           optB VARCHAR(50),
           optC VARCHAR(50),
           optD VARCHAR(50),
           correct VARCHAR(2));
INSERT INTO `QUES` VALUES (1,1,'Process of inserting an element to a stack is called','create','push','pop','insert','B'),(2,1,'Process of deleting an element from a stack is called','delete','remove','destroy','pop','D');
-- Admin Tables End           

CREATE TABLE USER
          (id varchar(11) PRIMARY KEY,
           email varchar(30) NOT NULL,
           username varchar(30) NOT NULL,
           password varchar(30) NOT NULL,
           stream varchar(5),
           sem varchar(5), 
           division varchar(5));
INSERT INTO USER VALUES('augu','augustinetharakan12@gmail.com','augu','augu','U');

DROP TABLE IF EXISTS USER_RESPONSE;
CREATE TABLE USER_RESPONSE
          (user_id varchar(11),
           test_id INTEGER NOT NULL,
           question_id INTEGER NOT NULL, 
           response VARCHAR(2));

CREATE TABLE TEST_REPORT(
          user_id varchar(60) NOT NULL, 
          test_id varchar(60) NOT NULL,
          mark decimal(5,2));
COMMIT;
