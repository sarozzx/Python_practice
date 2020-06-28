# Write a Python function to find the Max of three numbers.

def max1(list):
    return max(list)


list=[]
for i in range(3):
    x=int(input("Enter number : "))
    list.append(x)

max_num=max1(list)

print("the max is : ",max_num)