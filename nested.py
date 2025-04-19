# Write a Python program to check if a player can unlock the next level based on score, coins, and time.
"""score=int(input("Enter Your Score:- "))
coin=int(input("Enter Coins:- "))
time=int(input("Enter Time:- "))
if score>=100:
    if coin>=50:
        if time<=5:
            print("Level Unlocked!")
        else:
            print("Be fast next time!")
    else:
        print("Be more coins!")
else:
    print("Be more high score!")
"""
# Question:Write a Python program that checks whether a person is eligible to travel abroad. The person must have a passport, a visa, and flight tickets. Ask the user for input (Y/N) for each of these three conditions. If the person has all three, print "eligible". Otherwise, print the appropriate reason why they are not eligible.
"""passport=input("Pasport(Y/N):-").title()
visa=input("Visa(Y/N):-").title()
flight_t=input("Flight Tikets(Y/N):-").title()
if passport=="Y":
    if visa=="Y":
        if flight_t=="Y":
            print("eligible")
        else:
            print("Not eligible for flight")
    else:
         print("Not eligible for visa")
else:
     print("Not eligible for passport")
     
"""
    