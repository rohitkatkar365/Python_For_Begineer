import random

while True:
    c = (int(input("Enter You Number ")))
    rc = random.randrange(1,101)
    if c == rc:
        print("You Win")
        break
    elif c != rc:
        print("Random Number Is : ",rc)
        if rc > c:
            print("You Guess Is Small")
        else:
            print("You Guess IS High")
