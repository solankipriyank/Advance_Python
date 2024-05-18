'''Write a Python program to count the frequency of words in a file'''

from collections import Counter
file=open("abc.txt")
p=file.read().split()
print(Counter(p))
file.close()
