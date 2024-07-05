# Use Case: When you want the loop to execute at least once regardless of the condition.
# Python does not have a built-in do-while loop like some other languages.

i = 0

while True:
    print(i)
    i+=1
    if i >= 5:
        break
print(i)