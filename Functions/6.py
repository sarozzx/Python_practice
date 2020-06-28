# Write a Python function to check whether a number is in a given range.

def range_check(n):
    if n in range(1,7):
        print( n, " is in the range")
    else :
        print("The number is outside the given range.")

x=int(input("enter a number"))
range_check(x)