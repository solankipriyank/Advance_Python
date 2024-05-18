'''Write a Python program to read a file line by line and store it into a list'''

file=open("abc.txt")
a=file.readlines()
lst=[]
for i in range(len(a)):
    lst.append(a[i])
print(lst)      
file.close()
