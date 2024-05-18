'''Write a Python program to append text to a file and display the text'''

p= open("file.txt","a")
str = input("Enter Data TO Append  In file.txt : ")
p.write(str)
p = open("file.txt","r")
print(p.read())
p.close()
