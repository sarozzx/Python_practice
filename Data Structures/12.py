# Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.

def case(s):
    print("In Upper Cases : "+s.upper())
    print("In lower Cases : "+s.lower())


s=str(input("Enter a string"))
case(s)