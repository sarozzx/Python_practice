# Write a Python program to sum all the items in a list.

def sum(list):
    sum_lst=0
    for num in list:
        sum_lst+=num
    return sum_lst



list =[]

n=int(input("Enter number of items in list"))

for i in range(0,n):
    x=int(input())
    list.append(x)

print("The sum is  :",sum(list))