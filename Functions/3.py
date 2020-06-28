# Write a Python function to multiply all the numbers in a list.

def mul1(list):
    x=1
    for i in list:
        x*=i
    return x

list =[]

n=int(input("Enter number of items in list"))

for i in range(0,n):
    x=int(input())
    list.append(x)

print("THe product is ",mul1(list))