# Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.
def last(n):
    return n[-1]

def sort1(list):
    list.sort(key=last)
    return list



list =[]

n=int(input("Enter number of items in list and separate tuple item by comma"))

for i in range(0,n):
    x=str(input())
    list.append(tuple(x.split(",")))

print(sort1(list))