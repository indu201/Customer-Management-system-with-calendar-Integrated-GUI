USE student_db;
SHOW TABLES;
CREATE TABLE customer(
name VARCHAR(20), 
lastname VARCHAR(20),
contact BIGINT,
age int,
dob DATE, 
password VARCHAR(20),
gender VARCHAR(20),
city VARCHAR(20)
);

DESC customer;
SELECT * FROM customer;

CREATE TABLE teacher(
name VARCHAR(20), 
lastname VARCHAR(20),
contact BIGINT,
age int,
dob DATE, 
qualification VARCHAR(20),
gender VARCHAR(20),
city VARCHAR(20),
subject VARCHAR(20),
experience INT 
);

SELECT * FROM teacher;

CREATE TABLE students(
regid INT,
name VARCHAR(20), 
lastname VARCHAR(20),
contact BIGINT,
age int,
dob DATE, 
qualification VARCHAR(20),
gender VARCHAR(20),
city VARCHAR(20),
course VARCHAR(20),
fees INT 
);

SELECT * FROM students;

CREATE TABLE course(
coursename VARCHAR(20),
duration INT ,
coursefee INT,
teacher VARCHAR(20)
);

ALTER TABLE course
ADD COLUMN time VARCHAR(20),
ADD COLUMN coursemode VARCHAR(20),
MODIFY COLUMN duration VARCHAR(20);


SELECT * FROM course;