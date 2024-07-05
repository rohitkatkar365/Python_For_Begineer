import sys

import pymysql as p

try:
    myobj = p.connect(
        host = "localhost",
        user = "root",
        password = ""
    )

    cursor = myobj.cursor()

    id = ((input("Enter Id Which You Want To Update  :")))
    query = "UPDATE college.student set s_name=%s where s_id=%s"
    data = ("Rockey",id)

    cursor.execute(query,data)
    myobj.commit()

    print("Data Update Successfully")
except:
    print(sys.exc_info()[1])
finally:
    myobj.close()
    cursor.close()