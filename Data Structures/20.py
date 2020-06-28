# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.

def count_str(list):
    count=0
    for n in list:
        if len(n)>=2 and n[0]==n[-1]:
            count+=1
    return count


list =[]

n=int(input("Enter number of items in list"))

for i in range(0,n):
    x=str(input())
    list.append(x)

print("The required strings are : ",count_str(list))