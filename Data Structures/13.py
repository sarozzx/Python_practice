# Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

items=input("Enter words separated by comma : ")
word=[]
for words in items.split(","):
    word.append(words)
word.sort()
for words in word:
    print(words)