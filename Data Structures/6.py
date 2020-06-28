# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

def not_poor(str):
    not1 =str.find("not")
    poor =str.find("poor")
    if poor>not1 and poor>0 and not1>0:
        str=str.replace(str[not1:(poor+4)],"good")
        return str
    else:
        return str
str=input("Enter your string : ")
print(not_poor(str))

