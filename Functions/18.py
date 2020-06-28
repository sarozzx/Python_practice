# Write a Python program to check whether a given string is number or not
# using Lambda.

check_number = lambda x:True if x.isnumeric() else False

a=str(input("Enter a string "))


print(check_number(a))