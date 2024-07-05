import sys


class OneDivsionError(Exception):
    def __init__(self):
        print("You Given Denomintor As 1 That Not Allowed")

try:
    num1 = (int(input("Enter A First Number : ")))
    num2 = (int(input("Enter A Sceond Number : ")))
    if(num2==1):
        raise OneDivsionError
    else:
        print(num1//num2)
except (OneDivsionError,ZeroDivisionError) as var:
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])