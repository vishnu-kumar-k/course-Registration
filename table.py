import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1607",
    use_pure=True,
    database="project"
)
c=mydb.cursor()
c.execute("create table admin name varchar(20),password varchar(20)")
c.execute("create table user name varchar(20),password(20),phone_number varchar(20),age varchar(10)")
c.execute("create table user_details(course_id varchar(10),user_id varchar(10))")
c.execute("create table course(name varchar(30),id varchar(10),duration varchar(30),price varchar(10),course_instructor varchar(30))")