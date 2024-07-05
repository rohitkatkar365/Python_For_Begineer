import sys

import pymysql as p

try:
    myobj = p.connect(
        host = "localhost",
        user = "root",
        password = "")

    cursor = myobj.cursor()

    print("{:<15} {:<20} {:<20} {:<20}".format("Student Id","Student Name","Student Class","Student Email"))
    query = "SELECT * FROM college.student"
    cursor.execute(query)
    sdata = cursor.fetchall()
    for s in sdata:
        print("{:<15} {:<20} {:<20} {:<20}".format(s[0],s[1],s[2],s[3]))

except:
    print(sys.exc_info()[1])
finally:
    myobj.close()
    cursor.close()