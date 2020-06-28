# Write a Python function to insert a string in the middle of a string.

def insrt_str(str, str1):
    x=int((len(str))/2)
    return str[:x] + str1 + str[x:]

str=input("Enter a even number string : ")
str1=input("Enter a string to insert at middle :")

print(insrt_str(str,str1))



