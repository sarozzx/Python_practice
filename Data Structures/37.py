# Write a Python program to multiply all the items in a dictionary.

def product(dict1):
    product=1
    for items in dict1:
        product*=int(dict1[items])
    return product


dict1={"a":123,"b":112,"c":345,"d":454}


print("the product is ",product(dict1))