import sys

import pymysql as p

try:
    # The p.connect() function establishes a connection to the MySQL database server. The parameters are:
    # host='localhost': Connect to the database server running on the local machine.
    # user='root': Use the root user account.
    # password='': The password for the root user (empty in this case).

    myobj = p.connect(
        host='localhost',
        user='root',
        password="")

    # myobj.cursor() creates a cursor object that allows us to execute SQL queries.

    cursor = myobj.cursor()

    # query = "CREATE DATABASE COLLEGE" defines a SQL query to create a database named COLLEGE.

    # query = "CREATE DATABASE COLLEGE"
    # query = "CREATE TABLE COLLEGE.student(s_id int primary key auto_increment,s_name varchar(100),s_class varchar(1),s_email varchar(100))"
    query = "INSERT INTO COLLEGE.student(s_name,s_class,s_email) values(%s,%s,%s)"
    # t = ('Rohit','B','xyz@gmail.com')
    # for insert many record
    # t1 = [('Ram', 'A', 'ram@gmail.com'), ('Krishna', 'B', 'krish@gmail.com')]

    # cursor.execute(db) executes the SQL query using the cursor object.

    # cursor.execute(query)
    # cursor.execute(query,(input(),input(),input()))
    # cursor.executemany(query, t1)

    myobj.commit()
    # print("Database Created") prints a message indicating that the database was created successfully.

    # print("Database Created")
    print("Data Inserted")
except:
    print(sys.exc_info()[1])
finally:
    #cursor.close()closesthcursorobject.
    # myobj.close() closes the connection to the database server.

    myobj.close()
    # cursor.close()
