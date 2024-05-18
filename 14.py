'''How many except statements can a try-except block have? Name Some
built-in exception classes:'''


try:
    for i in range(3):
        print(3/i)
except:
    print("You divided by 0")
    print(‘This prints because the exception was handled’)
