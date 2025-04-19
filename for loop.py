# Write a Python program that takes your name as input and prints it three times using a loop.
'''a=input("Enter Your Name: ")
for i in range(1,4):
    print("Your Name is:",a)'''



# Question:Write a Python program that takes your name and a number as input, and then prints your name the specified number of times using a loop.
'''a=input("Enter Your Name: ")
b=int(input("Enter a Number: "))
for i in range(0,b):
     print("Your Name is:",a)'''


# Question:Write a Python program that takes your name as input and prints each character of your name on a new line.
'''a=input("Enter Yopur Name: ")
for i in a:
    print(i)'''



# Question:Write a Python program that takes a number and your name as input, then prints each character of your name repeatedly based on the input number.
'''num=int(input("Enter a Number: "))
name=input("Enter Your Name: ")
for nu in range(0,num):
    for nam in name:
        print(nam)'''



# Write a Python program that takes a number between 1 and 12 as input and prints its multiplication table from 1 to 12.
'''a=int(input("Enter Your Name between 1 to 12: "))
for i in range(1,13):
    an=i*a
    print(i,"x",a,"=",an)'''


# Write a Python program that takes a number below 50 as input and prints all numbers starting from 50 down to the input number.
'''a=int(input("Enter a Number below 50: "))
for i in range(50,a-1,-1):
    print(i)'''

# Write a Python program that takes your name and a number less than 10 as input. If the number is less than 10, it prints your name that many times; otherwise, it prints "Too High" three times.
'''''
a=input("Enter Your Name: ")
b=int(input("Enter a Number Less then 10: "))
if b<10:
    for i in range(0,b):
        print(a)
else:
        for i in range(0,3):
           print("Too High")'''