# Write a Python program to sort a list of dictionaries using Lambda.

list=[{"dance":123,'num':244},{"music":111,'num':54},{"sports":144,'num':523}]

list1=sorted(list,key= lambda a:a['num'])

print(list1)
