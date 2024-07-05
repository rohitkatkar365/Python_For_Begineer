try:
    age = (int(input()))
    if age < 0:
        raise ValueError("Give Age Is In Postive")
    print(age)
except ValueError as var:
    print(var)

