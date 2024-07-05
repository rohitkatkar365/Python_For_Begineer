# Use Case: When you don't know the number of iterations in advance and need to continue looping until a condition changes.

# Q1 : sum of n first natural number

n = (int(input()))
sum = 0
i = 0
while i < n:
    sum+=i
    i+=1

print(sum)