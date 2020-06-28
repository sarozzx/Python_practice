# Write a Python program to slice a tuple.

x=tuple(input("Enter tuple").split(","))

print("the tuple is : ",x)

y=int(input("Enter first slice number :"))
z=int(input("Enter second slice number :"))

slice=x[y:z]

print(slice)