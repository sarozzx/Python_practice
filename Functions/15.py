# Write a Python program to filter a list of integers using Lambda.

list1=[1,2,3,4,5,6,7,8,9]

even=list(filter(lambda x: x%2==0,list1))

print(even)