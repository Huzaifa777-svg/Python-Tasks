# Question:1 Write a Python program that prompts the user to enter a number with many decimal places. Multiply that number by 2 and display the result.
''' a=float(input("Enter a number with lot of decimal place: "))
c=a*2
print(c)'''

# Question:Write a Python program that:Prompts the user to enter a number with many decimal places.Multiplies that number by 2.Prints the result.(Optional) Also print the result rounded to 2 decimal places.
'''a=float(input("Enter a number with lot of decimal place: "))
c=a*2
print(c)
print(round(c,2))'''

# Write a Python program that Imports the math module using an alias.Stores the value of π (pi) in a variable.Prints the value of π rounded to 5 decimal places

'''import math as m
p=m.pi
print(round(p,5))'''

# Question:Write a Python program that takes an integer greater than 500 as input and prints its square root rounded to 2 decimal places.


'''import math as m
a=int(input("Enter a integer that is over 500: "))
b=m.sqrt(a)
print((round(b,2)))'''

# Question:Write a Python program that takes the radius of a circle as input and calculates the area using π, then prints the result.

'''import math as m
a=int(input("Enter Radius of circle: "))
b=m.pi*(a**2)
print(b)'''

# Question:Write a Python program that creates a deep copy of a set, assigns it to another variable, and then adds an element to the second set. Print both sets to observe the result.
"""

import copy

a={1,2,3,5,90,6,2}

a_c=copy.deepcopy(a)
b=a_c
print(b)
b.add(40)
print(b)
"""


