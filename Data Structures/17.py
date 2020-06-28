# Write a Python program to multiplies all the items in a list.

def mul(list):
    mul_lst=1
    for num in list:
        mul_lst*=num
    return mul_lst



list =[]

n=int(input("Enter number of items in list"))

for i in range(0,n):
    x=int(input())
    list.append(x)

print("The product is  :",mul(list))