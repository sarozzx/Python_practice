# Write a Python program to check whether all dictionaries in a list are empty or
# not.

def check(list):
    if list:
        for items in list:
            if items:
                return "False"
        return "True"


list1=[{},{},{}]

list2=[{1,2},{},{}]

print(check(list1))
print(check(list2))


