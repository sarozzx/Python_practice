# Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

def func(n):
    return lambda a:a*n

result=func(2)
print("the result : ",result(10))