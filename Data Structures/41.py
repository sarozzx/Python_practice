# Write a Python program to convert a tuple to a string.

x=tuple(input("Enter tuple").split(","))

print("the tuple is : ",x)
str=""
for items in x:
    str+=items
print(str)