# Write a Python program to check a list is empty or not.

def check_emp(list):
    if not list:
        print("it is an empty list")
    else:
        print("it is not an empty list")
list =[]

n=int(input("Enter number of items in list"))

for i in range(0,n):
    x=input()
    list.append(x)

check_emp(list)