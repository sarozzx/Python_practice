# Write a Python program to reverse a string.

def rev(str):
    x=len(str)
    y=str[x::-1]
    return y


str=str(input("Enter a string: "))

str=rev(str)

print(str)