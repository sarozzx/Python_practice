# Write a Python program to iterate over dictionaries using for loops.

def a1(dict1):
    for key,value in dict1.items():
        print(key," has value ",value)

dict1 = {}

n=int(input("Enter number of items in dictionary"))

for i in range(n):
    x=str(input("key"))
    y=str(input("value"))
    dict1[x]=y

a1(dict1)
