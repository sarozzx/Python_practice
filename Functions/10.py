# Write a Python program to print the even numbers from a given list.


def even1(n):
    list=[]
    for items in n:
        if items%2==0:
            list.append(items)
    return list

list1=[]

x=int(input("Enter the number of elements in the list: "))

for i in range(x):
    y=int(input())
    list1.append(y)

list1=even1(list1)

print(list1)