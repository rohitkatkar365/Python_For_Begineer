# Different type of argument in python
'''
1. Postional Argument
2. Default Argument
3. Keyword Argument
4. Vaiable-length argument :
    i. Arbitrary Keyword Arguments (**kwargs)
    ii. Arbitrary Positional Arguments (*args)
'''

'''
Positional Arguments:
These are the most common type of arguments and are passed to a function in the correct positional order.
'''
def info(name,message):
    print(message +","+name)

info("Rohit","Good Afternoon")

'''
Keyword Arguments:
These arguments are passed to the function by explicitly stating the parameter name and value.
'''

def greet(name,message):
    print(message +","+name)

greet(name="Rohit",message="Good Morning")

'''
Default Arguments:
These arguments assume a default value if a value is not provided in the function call.
'''

def sum(a,b=2):
    print(a+b)

sum(1)

'''
Variable-length Arguments:
These allow you to pass an arbitrary number of arguments to a function
'''
# Arbitrary Positional Arguments (*args)
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")

# Arbitrary Keyword Arguments (*args)
def greet(**kwargs):
    for name, message in kwargs.items():
        print(f"Hello, {name}! {message}")

greet(Alice="Good morning!", Bob="How are you?")
