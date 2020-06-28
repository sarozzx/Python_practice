# Write a Python function that takes a list of words and returns the length of the
# longest one.
s=str(input("Enter a string :"))
def long_word(thislist):
    le=thislist[0]
    for n in thislist:
        if len(n)>len(le):
            le=n
    return le
# thislist=["apple", "banana", "cherry"]

input_string = input("Enter a list elements separated by space ")

print("\n")
userList = input_string.split()

a=(long_word(userList))
print(a)