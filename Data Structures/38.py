# Write a Python program to remove a key from a dictionary.
dict1 = {}

n=int(input("Enter number of items in dictionary"))

for i in range(n):
    x=str(input("key"))
    y=str(input("value"))
    dict1[x]=y

print(dict1)

q=str(input("which key do u wanna remove"))

del dict1[q]

print(dict1)
