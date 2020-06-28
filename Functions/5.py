# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

def facto(x):
    if(x==0):
        return 0
    if(x==1):
        return 1
    return x*facto(x-1)

y=int(input("Enter a number : "))

print("The factorial of ",y,"is",facto(y))