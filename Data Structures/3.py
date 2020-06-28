# Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
s=str(input("Enter a string :"))
def charrep(str):
    char = str[0]
    str= str.replace(char,"$")
    str= char + str[1:]
    return str;
print(charrep(s))
