# Write a Python script to check whether a given key already exists in a
# dictionary.



dict1 = {}

n=int(input("Enter number of items in dictionary"))

for i in range(n):
    x=str(input("key"))
    y=str(input("value"))
    dict1[x]=y

def check_key(x):
    if x in dict1:
        print("exists")
    else:
        print("doesnt exist")

check_key(5)
check_key(6)