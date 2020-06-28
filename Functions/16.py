# Write a Python program to square and cube every number in a given list of
# integers using Lambda.

list1=[]

x=int(input("Enter number of items in list : "))
for i in range(x):
    y=int(input())
    list1.append(y)

print(list1)

print("square :")

square=list(map(lambda a:a*a,list1))

cube=list(map(lambda a:a**3,list1))

print(square)

print("cube: ",cube)