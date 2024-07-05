# for loop use when you want to perform repetitive task
# Use Case: When you know the number of iterations in advance or when you need to iterate over a sequence
# (like a list, tuple, string, or range).

# Q1 : sum of n first natural number

n = (int(input()))
sum = 0

for i in range(0,n):
    sum +=i

print(sum)

# Q2 : Traverse list

li = [1,2,3,4,5,6]
for i in li:
    print(i)