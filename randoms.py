# 1.You have a list:names = ['Alice', 'Bob', 'Charlie', 'Diana']Write a Python program to randomly shuffle the order of names in the list.
'''import random as ran
names = ['Alice', 'Bob', 'Charlie', 'Diana']
ran.shuffle(names)
print(names)'''

# 2.Given a list of colors:colors = ['red', 'blue', 'green', 'yellow']Write a Python statement to randomly select and print one color from the list.
'''import random
colors=['red','blue', 'green', 'yellow']
print(random.choice(colors))'''


#3.Write a program to generate and print a random integer between 1 and 100 (both inclusive).

"""import random as ran
print(ran.randint(1,100))
"""

#4.Write a Python statement to generate and print a random floating-point number between 0 and 1.
"""import random
print(random.random())"""