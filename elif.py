# write a program to check character is an Alphabet Digit or special character ?
'''an=input("Enter: ")
if len(an)!=1:
    print("Enter One Digit Only!")
else:
    asc=ord(an)
if 65<=asc<=90 or 97<=asc<=122:
    print("Alphabets")
elif 48<=asc<=57:
    print("Number")
else:
    print("Special Character!")'''

#Create a program to calculate the discount based on a user purchase amount using if-else statements(e.g 10% discount for a purchase over 100$,20% for over 200$,etc)
'''inp=int(input("Enter Your Amount: "))
if inp>100:
    dis=inp*0.10
    print(f"Your Amount After Discount is: {inp-dis}")
elif inp>200:
    dis=inp*0.20
    print(f"Your Amount After Discount is: {inp-dis}")
elif inp>300:
    dis=inp*0.30
    print(f"Your Amount After Discount is: {inp-dis}")
elif inp>400:
    dis=inp*0.40
    print(f"Your Amount After Discount is: {inp-dis}")
elif inp>500:
    dis=inp*0.50
    print(f"Your Amount After Discount is: {inp-dis}")
else:
    print("Your Amount is:",inp)'''

#write a program to take a three number as input and finds the largest amoung them using if-else statement

'''n1=int(input("Enter a Number 1: "))
n2=int(input("Enter a Number 2: "))
n3=int(input("Enter a number 3: "))
if n1>n2 and n1>n3:
    print("Large Number 1")
elif n2>n1 and n2>n3:
    print("The Largest Number 2")
else:
    print("The largest Number is 3")
'''

# write a program to calculate the grade the grade of a student based on their marks using if-else
'''marks=int(input("Enter Your Marks:: "))
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
elif marks>=90 :
    print("A+")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")
elif marks<=50:
    print("F")
else:
    print("Invalid!")'''