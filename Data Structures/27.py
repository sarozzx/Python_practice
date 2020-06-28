# Write a Python program to replace the last element in a list with another list.

def con_list(list1,list2):
    list1[-1:]=list2
    return list1

list1 =[]

n=int(input("Enter number of items in list1"))

for i in range(0,n):
    x=str(input())
    list1.append(x)

list2 =[]

n=int(input("Enter number of items in list2"))

for i in range(0,n):
    x=str(input())
    list2.append(x)

list1=con_list(list1,list2)

print(list1)