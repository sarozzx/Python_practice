# Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.
s=str(input("Enter a string :"))
def ing_change(str):
    if len(str)<3:
        return str
    else:
        if str[-3:]== "ing":
            return str+"ly"
        else:
            return str+"ing"
print(ing_change(s))
# print(ing_change("abc"))
# print(ing_change("string"))
# print(ing_change("ab"))