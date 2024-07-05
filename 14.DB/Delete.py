import sys

import pymysql as p

try:
    myobj = p.connect(
        host = "localhost",
        user = "root",
        password = ""
    )

    cursor = myobj.cursor()

    id = ((input("Enter Id Which You Want To Delete  :")))
    query = "DELETE FROM college.student WHERE s_id=%s"

    cursor.execute(query,id)
    myobj.commit()

    print("Data Delete Successfully")
except:
    print(sys.exc_info()[1])
finally:
    myobj.close()
    cursor.close()