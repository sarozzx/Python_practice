# Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.
s=str(input("Enter 1st string :"))
s1=str(input("Enter 2nd string :"))
def single_str(str1,str2):
    st1=str2[:2]+str1[2:]
    st2=str1[:2]+str2[2:]
    str=st1+" "+st2
    return str
print(single_str(s,s1))