# Write a Python program to remove the n
# th index character from a nonemptystring.

def remov(str,j):
    if not str:
        print("its an empty string ")
    if j>len(str):
        print("given index isnt in the string")
    else:
        str=str[0:j]+str[j+1:]
        return str
str=str(input("enter the string : "))
j=int(input("enter the index : "))
str1=remov(str,j)
print(str1)