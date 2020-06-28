# Write a Python program to clone or copy a list.
orginal_list =[]

n=int(input("Enter number of items in list"))

for i in range(0,n):
    x=input()
    original_list.append(x)

new_list = list(original_list)
print(original_list)
print(new_list)