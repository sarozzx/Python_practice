# Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.

def exchang(str):
    str=str[-1]+str[1:-1]+str[0]
    return str
str=str(input("Enter the string: "))
str1=exchang(str)
print(str1)