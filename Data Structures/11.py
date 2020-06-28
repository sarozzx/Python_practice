# Write a Python program to count the occurrences of each word in a given
# sentence.

def wordfreq(s):
    word_count={}
    words=s.split()
    for word in words:



        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count
s=str(input("Enter a string"))
print(wordfreq(s))