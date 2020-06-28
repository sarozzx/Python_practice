# Write a Python program to remove duplicates from a list.
def remov_dup(list):
    x=[]
    for z in list:
        if z not in x:
            x.append(z)
    return x

list =[]

n=int(input("Enter number of items in list"))

for i in range(0,n):
    x=input()
    list.append(x)

print("The new list  :",remov_dup(list))