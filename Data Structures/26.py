# Write a Python program to insert a given string at the beginning of all items in
# a list.

def add_string(list,str):
    for i in range(0,len(list)):
        list[i] =str+list[i]



    return list
list =[]

n=int(input("Enter number of items in list"))

for i in range(0,n):
    x=str(input())
    list.append(x)

str1=str(input("Enter the string :"))

list=add_string(list,str1)

print(list)