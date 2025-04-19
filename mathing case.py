# Q2: Write a program that asks the user to enter the name of an animal (e.g., Cat, Dog, Monkey, Cow).
# Use match-case to print the sound of the entered animal.

"""sound=input("Enter Animal: ").title()
match sound:
    case "Cat":
        print("Meo Meo")
    case "Dog":
        print("bow-wow")
    case "Monkey":
        print ("ooh-ooh-ah-ah")
    case "Cow":
        print("Moo")
    case defualt:
        print("Try Again!")

"""
# Q1: Write a program that takes two numbers and an operator (+, -, *, /) from the user, 
# then uses match-case to perform the selected operation.
"""
num1=int(input("Enter A Number 1: "))
num2=int(input("Enter A Number 2: "))
op=input("Enter Operator Like +,-,*,/ : ")
match op:
    case "+":
        print(f"Your Answere is: {num1+num2}")
    case "-":
        print(f"Your Answere is: {num1-num2}")
    case "/":
        print(f"Your Answere is: {num1//num2}")
    case "*":
        print(f"Your Answere is: {num1*num2}")
    case defult:
        print("Invalid operator!")
"""
# Q3: Write a program that takes a number (1-7) from the user and prints the name of the corresponding day using match-case.
"""
day=int(input("Enter A Day Number 1-7: "))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case defult:
        print("Invalid Number!")"""
"""a="10"
y=5
print(a*y)"""
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}