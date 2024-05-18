'''Write a Python program to count the number of lines in a text file'''

file=open("abc.txt")
p=file.readlines()
print(len(p))
file.close()
