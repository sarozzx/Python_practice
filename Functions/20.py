# Write a Python program to find intersection of two given arrays using
# Lambda.

a1=[4,5,67,892,1,2]
a2=[5,6,7,1,3,7]

intersec=list(filter(lambda x:x in a1,a2))

print(intersec)