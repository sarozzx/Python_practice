# Write a Python script to add a key to a dictionary.

dict1 = {}

n=int(input("Enter number of items in dictionary"))

for i in range(n):
    x=str(input("key"))
    y=str(input("value"))
    dict1[x]=y

print(dict1)

q=str(input("add a new key"))
r=str(input("its value"))
dict1[q]=r
