import random as ran
print("*** Welcome To MHS Number Guessing Number ***")
while True:
    guess_num=ran.randint(1,500)
    attempt=0
    while True:
        User_Guess=int(input("Enter Your Guessing Number:- "))
        attempt+=1
        if User_Guess<guess_num:
            print("Too Low ! Plaese Try")
        elif User_Guess>guess_num:
            print("Too High ! Plaese Try") 
        else:
            print("Congrats You Have Guess a number",guess_num,"attempt",attempt)
            break
    play_again=input("Do You Want To Play Again (y/n)").title()
    if play_again!="Y":
        print("Good Bye!")
        break
