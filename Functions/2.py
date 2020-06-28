# Write a Python function to sum all the numbers in a list.

def sum1(list):
    return sum(list)

list =[]

n=int(input("Enter number of items in list"))

for i in range(0,n):
    x=int(input())
    list.append(x)

print("THe sum is ",sum1(list))