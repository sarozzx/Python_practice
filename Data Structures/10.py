# Write a Python program to remove the characters which have odd index
# values of a given string.

def remov(str):
    x=''
    for n in range(len(str)):
        if n%2==0:
            x=x+str[n]
    return x
str=str(input("Enter the string: "))
str1=remov(str)
print(str1)