# Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

dict1={}

n=int(input("input n : "))

for i in range(n):
    x = i+1
    y = x*x
    dict1[x] = y

print("the dictionary is ",dict1)