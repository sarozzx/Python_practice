# Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys

dict1={}

for i in range(15):
    x = i+1
    y = x*x
    dict1[x] = y

print("the dictionary is ",dict1)