# Write a Python program to get the smallest number from a list.

def small(list):
    x=list[0]
    for n in list:
        if n<x:
            x=n
    return x

list =[]

n=int(input("Enter number of items in list"))

for i in range(0,n):
    x=int(input())
    list.append(x)

print("The largest is  :",small(list))