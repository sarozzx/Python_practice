# Write a Python program to sum all the items in a dictionary.

def sum(dict1):
    sum=0
    for items in dict1:
        sum+=int(dict1[items])
    return sum


dict1={"a":123,"b":112,"c":345,"d":454}

# print("the sum is ",sum(dict1.values()))

print("the sum is ",sum(dict1))