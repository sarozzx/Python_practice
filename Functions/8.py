# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

def uniq_list(list1):
    list=[]
    for items in list1:
        if items not in list:
            list.append(items)
    return list
list1=[]

x=int(input("Enter the number of elements in the list: "))

for i in range(x):
    y=input()
    list1.append(y)

list1=uniq_list(list1)

print(list1)