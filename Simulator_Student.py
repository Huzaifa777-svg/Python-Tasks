print("*** Welcome To Student Simulation Game *** ")
choice=int (input("""select action you want to Perform:-
            1. Study
            2. Rest 
            3. Exercise
"""))
match choice:
    case 1:
        print("you select an option study")
        s_choice=int(input("""you want to study alone or with friends:- 
                    1.Alone
                    2.Friends
                           """))
        if s_choice ==1:
            print("you select an option alone\n working hard!")
        elif s_choice==2:
            print("you select an option friends\n only study!")
        else:
            print("Invalide choice!")
  
    case 2:
        print("you select  an option rest")
        s_choice=int(input("""you want to rest sleep or outing:- 
                    1.Sleep
                    2.Outing
                           """))
        if s_choice ==1:
            print("you select an option sleep\n Sweet Dreams!")
        elif s_choice==2:
            print("you select an option outing\n Enjoy Nature!")
        else:
            print("Invalide choice!")
    
    case 3:
        print("you select an option Exercise")
        s_choice=int(input("""you want to exercise machinery  or with manually :- 
                    1.machinery
                    2.manually 
                           """))
        if s_choice ==1:
            print("you select an option machinery \n Working Hard!")
        elif s_choice==2:
            print("you select an option manually \n Best Of Luck!")
        else:
            print("Invalide choice!")

    case defult:
        print("Try Again!!")
print("Program Successfully Run")

