# Write a Python program to find if a given string starts with a given character
# using Lambda.

start= lambda x:True if x.startswith('H') else False

x=input("Enter a string ")
print(start(x))