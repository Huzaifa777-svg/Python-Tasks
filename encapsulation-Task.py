#Q1: Write a class Student with private attributes name and marks. Create setter and getter methods to modify and access these attributes.
""""class Student:
    def __init__(self, name="", marks=0):
        self.__name = name     
        self.__marks = marks   

    
    def set_name(self, name):
        self.__name = name

    # Getter method for name
    def get_name(self):
        return self.__name

    
    def set_marks(self, marks):
        self.__marks = marks

   
    def get_marks(self):
        return self.__marks


student1 = Student()
student1.set_name("Huzaifa")
student1.set_marks(92)

print("Student Name:", student1.get_name())
print("Student Marks:", student1.get_marks())""""

# Q2: Identify the error in the following code related to encapsulation:

# class Car:
#     def __init__(self, brand):
#         self.__brand = brand

# car = Car("Toyota")
# print(car.__brand)

# Ans:-
# This will result in an AttributeError, as __brand is a private attribute and cannot be accessed directly. Python internally changes __brand to _Car__brand to avoid name clashes in subclasses, but you should not access it directly.

#Q3: What will be the output of the following code?

# class Test:
#     def __init__(self):
#         self.__x = 10

# obj = Test()
# print(obj.__x) 

"""AttributeError: 'Car' object has no attribute '__brand'"""

# Q4 Create a class Student with private attributes __name, __roll_no, and __marks.
# Add:

# A method to set student data

# A method to display the data

# Validation that marks must be between 0 and 100

class Student:
    def __init__(self):
        self.__name = ""
        self.__roll_no = ""
        self.__marks = 0

    def set_data(self, name, roll_no, marks):
        if 0 <= marks <= 100:
            self.__name = name
            self.__roll_no = roll_no
            self.__marks = marks
        else:
            print("Invalid marks! Marks must be between 0 and 100.")

    def display_data(self):
        print(f"Name: {self.__name}")
        print(f"Roll No: {self.__roll_no}")
        print(f"Marks: {self.__marks}")


student1 = Student()
student1.set_data("Ali", "BSCS123", 85)
student1.display_data()


student2 = Student()
student2.set_data("Sara", "BSCS124", 120)  
student2.display_data()
