'''Write a Python program to copy the contents of a file to another file'''

with open('Tops.txt','r') as topsfile, open('abc.txt','a') as abcfile: 
    for line in topsfile:
       secondfile.write(line)
