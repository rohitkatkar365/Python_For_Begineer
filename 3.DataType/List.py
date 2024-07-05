# li = [1,2,3,"R","Ram"]

# print(f"{li} is type of : ",type(li))
# print(li[0])
# print(li[0 : 2 : 2])
# print(li[-1])
# print(li[-1::-1])

# Travese list
# for i in range(0,len(li)):
#     print(li[i])

# for i in li:
#     print(i)

# for i in range(len(li)-1,-1,-1):
#     print(li[i])

# Take user i/p
# list compherison
# e = ((input()))
# li1 = [int(i) for i in e.split()]
# print(li1)
# this is slower than list compherison
# n = (int(input()))
# for i in range(0,n):
#     ele = (int(input()))
#     li1.append(ele)
# print(li1)

# del,pop,remove,clear
# del li
# print(li)

# print(li.pop()) #delete last element
# # print(li.pop(1)) # delete elenement at index
#
# li.remove(1)
# print(li)

# claer list
# print(li.clear())

# count,max,min,sort,reverse,index
# li = [10,2,0,30,2,10,2,5,6]
# print(li.count(2))
# li.reverse()
# print(li)
# print(max(li))
# print(min(li))
# li.sort()
# print(li)
#
# li.extend([100,200,300])
# print(li)

a = [1,2,3,4]
b = [1,2,3,4,5]
for i,j in zip(a,b):
    print(i,j)



