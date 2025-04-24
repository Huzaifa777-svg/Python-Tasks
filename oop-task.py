# Create an abstract class Employee with:
# An abstract method calculate_salary()

# Then, implement it in:

# FullTimeEmployee

# PartTimeEmployee

# Each class should return a different salary calculation logic.

"""from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, basic, allowance, deduction):
        self.basic = basic
        self.allowance = allowance
        self.deduction = deduction

    def calculate_salary(self):
        return self.basic + self.allowance - self.deduction

class PartTimeEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


emp = [
    FullTimeEmployee(15000, 1000, 200),
    PartTimeEmployee(6, 120)
]

for e in emp:
    print(e.calculate_salary())

"""
# Each class should return a different salary calculation logic.

# 3. Create an abstract class Shape with an abstract method area().
# Implement the class for:

# Rectangle (with width and height)

# Circle (with radius)

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

obj=[Rectangle(12,23),Circle(12)]
for i in obj:
    i.area()

