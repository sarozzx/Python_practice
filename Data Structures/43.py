# Write a Python program to remove an item from a tuple.

x=tuple(input("Enter tuple").split(","))

print("the tuple is : ",x)

y=int(input("which index element do you want to remove : "))

x=x[:y]+x[(y+1):]

z=str(input("which element do you want do remove  :"))

list1=list(x)

list1.remove(z)

x=tuple(list1)

print(x)