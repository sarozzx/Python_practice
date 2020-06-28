# Write a Python program to find the index of an item of a tuple.
x=tuple(input("Enter tuple").split(","))

print(x)

y=str(input("Enter item you want to find index of "))

z=1

for i in range(len(x)):
    if(x[i]==y):
        print("the index is :",i)
        z=2
        break
if(z==1):
    print("the item is not in the tuple")