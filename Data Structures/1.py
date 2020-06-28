# Write a Python program to count the number of characters (character
# frequency) in a string.

def charfreq(s):
    cha={}
    for n in s:



        if n in cha:
            cha[n]+=1
        else:
            cha[n]=1
    return cha
s=str(input("Enter a string"))
print(charfreq(s))