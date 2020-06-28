# Write a Python function to create the HTML string with tags around the
# word(s).

def creat_tags(tag, str):
	return "<%s>%s</%s>" % (tag, str, tag)
    # return "<"+tag+">"+str+"</"+tag+">"
tag=input("Enter tag : ")
str=input("Enter string : ")
print(creat_tags(tag, str))
