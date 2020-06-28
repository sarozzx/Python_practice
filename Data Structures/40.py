# Write a Python program to add an item in a tuple.

x=tuple(input("Enter tuple").split(","))

print("the tuple is : ",x)

y=input("Enter a item to add to the tuple :")

x=x+(y,)

print("The Tuple is : ",x)