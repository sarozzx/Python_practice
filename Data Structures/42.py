# Write a Python program to convert a list to a tuple.

list =[]

n=int(input("Enter number of items in list"))

for i in range(0,n):
    x=str(input())
    list.append(x)


x=tuple(list)

print(x)