'''Write a Python program to read first n lines of a file.'''

n = int(input("Enter Lines To Read : "))
p = open("file.txt","r")
for i in range(n):
	print(p.readline())
