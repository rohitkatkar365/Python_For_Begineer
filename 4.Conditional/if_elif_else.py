# if elif else is use when you want to check mutiple condition

num1 = (int(input("Enter First Number :")))
num2 = (int(input("Enter Second Number :")))
operation = (input("Enter Operation Which You Want To Perform : "))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
elif operation == '%':
    print(num1 % num2)
