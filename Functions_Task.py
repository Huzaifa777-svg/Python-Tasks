# 1- Find Maximum of Three Numbers
#Write a function max_of_three(a, b, c) that returns the largest of the three.
"""number1=int(input("Enter Number 1:- "))
number2=int(input("Enter Number 2:- "))
number3=int(input("Enter Number 3:- ")) 
def max_of_three(number_1,number_2,number_3):
    if number_1>number_2 and number_1>number_3:
        print("Number 1 is largest")
    elif number_2>number_1 and number_2>number_3:
        print("Number 2 is largest")
    else:
        print("Number 3 is largest")
    return number1,number2,number3

max_of_three(number1,number2,number3)
"""
# 2- Simple Interest Calculator
# Write a function simple_interest(p, r, t) that returns the simple interest using the formula SI = (p * r * t) / 100.
"""
Principal =int(input("Enter Principal:-"))
Rate=int(input("Enter Rate:-"))
Time=int(input("Enter Time:-"))
def SI(p,r,t):
    simple_interest=(p*r*t)/100
    return simple_interest
Formula=SI(Principal,Rate,Time)
print("Your Simple Inerest is:- ",Formula)
"""
# 3- Login System
# Write a function login(username, password) that checks:
# If username is "admin" and password is "1234", return "Login successful"Else return "Invalid credentials"

user_name=input("Enter Your User Name:- ")
user_password=int(input("Enter Password:-"))

def login_system(user_name,user_password):
    if user_name=="admin" and  user_password==1234:
        return "Login successful"
    else:
        return "Invalid credentials"
p=login_system(user_name,user_password)
print(p)



# 4- BMI Calculator
# Write a function bmi_category(weight_kg, height_m) that calculates BMI and returns:

# "Underweight" if BMI < 18.5

# "Normal" if 18.5 ≤ BMI < 25

# "Overweight" if 25 ≤ BMI < 30

# "Obese" if BMI ≥ 30

# BMI = weight / height²

"""
weigth_kg=float(input("Enter Weight:- "))
height_m=float(input("Enter Height:- "))

def bmi_category(weight_kg, height_m):
    BMI= weight_kg/height_m**2
    if BMI < 18.5:
        return"Underweight"
    elif 18.5 < BMI < 25:
        return"Normal"
    elif BMI > 30:
        return("Obese")
    else:
        return"Try Again!"
bmi=bmi_category(weigth_kg,height_m)
print(bmi)
    """

# 5- Custom Calculator
# Write a function calculate(a, b, operator) where operator is a string like "+", "-", "*", or "/". Return the result, or "Invalid operator" if unknown.

"""a=int(input("Enter Your Number 1:- "))
b=int(input("Enter Your Number 2:- "))
operator=input("Enter operator +,-,*,/ :- ")

def cal(a,b,op):
    if op=="+":
        return("Your Answere is:- ",a+b)
    elif op=="*":
        return("Your Answere is :- ",a*b)
    elif op=="-":
        return("Your Answere is :- ",a-b)
    elif op=="/":
        return("Your Answere is :- ",a/b)
    else:
        return "Invalid operator"
result=cal(a,b,operator)
print("Your Result is:-",result)"""
