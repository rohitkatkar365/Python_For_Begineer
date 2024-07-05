try:
    num1 = (int(input("Enter A First Number : ")))
    num2 = (int(input("Enter A Sceond Number : ")))
    if(num2==0):
        div = num2//num1
        print(div)
    else:
        print(num1//num2)
except:
    print("Divide By Zero Not Allowed")
else:
    print("You're Right")
finally:
    print("TRUE")
