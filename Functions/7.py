# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.

def calcu(str):
    up=0
    low=0
    for i in range(len(str)):
        if str[i].islower():
            low+=1
        if str[i].isupper():
            up+=1
    print("Uppercase numbers : ",up)
    print("lowerCase numbers : ",low)
x=input("Enter a string : ")

calcu(x)