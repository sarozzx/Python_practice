# Write a Python function that takes a number as a parameter and check the
# number is prime or not.

def prime1(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True

x=int(input("Enter a number to check if its prime "))
print(prime1(x))