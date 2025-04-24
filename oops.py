# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#     def sleep(self):
#         print("sleep")
# class Dog(Animal):
#     def make_sound(self):
#         print("Burk")
# class Cat(Animal):
#     def make_sound(self):
#        print("meo")
# animals=[Dog(),Cat()]
# for animal in animals:
#     animal.make_sound()
#     animal.sleep()
    

# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class FullTimeEmployee(Employee):
#     def __init__(self, basic, allowance, deduction):
#         self.basic = basic
#         self.allowance = allowance
#         self.deduction = deduction

#     def calculate_salary(self):
#         return self.basic + self.allowance - self.deduction

# class PartTimeEmployee(Employee):
#     def __init__(self, hours, rate):
#         self.hours = hours
#         self.rate = rate

#     def calculate_salary(self):
#         return self.hours * self.rate

# # Test
# emp = [
#     FullTimeEmployee(15000, 1000, 200),
#     PartTimeEmployee(6, 120)
# ]

# for e in emp:
#     print(e.calculate_salary())

from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Example usage
rect = Rectangle(4, 5)
print("Area of Rectangle:", rect.area())

circle = Circle(3)
print("Area of Circle:", circle.area())



