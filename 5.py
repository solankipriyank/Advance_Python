''' Write a Python program to read last n lines of a file.'''

file=open("abc.txt")
l=file.readlines()
print(l[-1:])
file.close()
