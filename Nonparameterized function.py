# Simple Quiz:Create a function start_quiz() that asks a question, takes user input inside the function, and gives feedback.
"""
def start_quiz():
    print("Welcome to the Quiz!")
    question = "What is the capital of Pakistan?"
    cor_ans = "Islamabad"
    
    # Ask the question
    user_answer = input(question + " ")

    # Check the answer and give feedback
    if user_answer.strip().lower() == cor_ans.lower():
        print("Correct! Well done.")
    else:
        print(f"Wrong! The correct answer is {cor_ans}.")

    # Ask for user feedback
    feedback = input("\nDid you like the quiz? Any feedback or suggestions? ")
    print("Thanks for your feedback!")
    print("You said:", feedback)

# Start the quiz
start_quiz()

"""


# Menu Display:Create a function show_menu that prints a list of food items available in a zoo canteen.
'''def show_menue ():
    print("""Snacks & Fast Food for zoo🥲:

Popcorn 🍿

French Fries 🍟

Burgers 🍔

Chicken Nuggets 🍗

Ice Cream 🍦

Cotton Candy 🍭

Beverages:

Soft Drinks 🥤

Fresh Juices 🍹

Bottled Water 💧

Tea & Coffee ☕

Healthy Options:

Fruit Salad 🍓🍍

Grilled Sandwiches 🥪

Veggie Wraps 🌯

Yogurt Cups 🥣""")
    
show_menue()
'''

# Motivation Booster:Create a function daily_motivation that prints a motivational quote when called.
'''def daily_motivation():
    print("Anger is never without a Reason, but seldom with a good One")
daily_motivation()'''