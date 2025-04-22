# Simple Inheritance
# 1-Create a class Animal with a method speak() that prints "Animal sound".
# Then create a class Dog that inherits from Animal.
# Task: Create a Dog object and call speak().

"""class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    pass
dog=Dog()
dog.speak()"""


# Method Overriding
# 2- Modify the Dog class to override the speak() method to print "Bark".
# Task: Show that Dog().speak() prints "Bark" instead of "Animal sound".

# Modified Dog class with overridden speak() method
"""class Dog(Animal):
    def speak(self):
        print("Bark")


dog = Dog()
dog.speak()  """


# 3- Multilevel Inheritance
# Class Grandparent → Parent → Child.
# Each class has a method describe() that prints its class name.
# Task: Override describe() in Parent. What happens when Child().describe() is called?

"""class Grandparent:
    def describe(self):
        print("Grandparent")
class Parent(Grandparent):
    def describe(self):
        print("Parent")
class Child(Parent):
    def describe(self):
        print("Child")
child=Child()
child.describe()
        """

# Multiple Inheritance
# Class Flyer has def move(): print("Flying").
# Class Walker has def move(): print("Walking").
# Class Bird inherits from both.
# Task: What does Bird().move() output? Explain why.
class Flyer:
    def move(self):
        print("Flying")

class Walker:
    def move(self):
        print("Walking")

class Bird(Flyer, Walker):
    pass

bird = Bird()
bird.move()
