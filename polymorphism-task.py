# Create a class Animal with a method speak(). Then create subclasses Cow and Sheep that override speak() with different sounds. Use a loop to call speak() on each object.
"""class Animal():
    def speak(self):
        pass
class Cow(Animal):
    def speak(self):
        print("moo")
class Sheep(Animal):
    def speak(self):
        print("baa")

Animals=[Cow(),Sheep()]
for ani in Animals:
    ani.speak()"""

# Create a class PaymentMethod with a method pay(amount). Then make two subclasses CreditCard and Cash that override pay() with different messages. Use polymorphism to handle different payment types.

class PaymentMethod:
    def pay(self, amount):
        print(f"Paying {amount} using a generic payment method.")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card.")

class Cash(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} in Cash.")

def process_payment(payment_method, amount):
    payment_method.pay(amount)

payment1 = CreditCard()
payment2 = Cash()

process_payment(payment1, 1000) 
process_payment(payment2, 500)  

# Create a class Employee with a method work(). Then make two subclasses Manager and Developer, both overriding the work() method. Write a loop that runs work() on both objects.

class Employee:
    def work(self):
        print("Employee is working.")


class Manager(Employee):
    def work(self):
        print("Manager is overseeing the team.")


class Developer(Employee):
    def work(self):
        print("Developer is writing code.")

employees = [Manager(), Developer()]

for employee in employees:
    employee.work()
