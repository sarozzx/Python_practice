# Write a Python program to sort a list of tuples using Lambda.


list=[("dance",4133),("music",123),("sports",63563)]
list.sort(key = lambda x:x[1] )
print(list)