'''
RULES OF THIS GAME

Choice 1	    Choice 2	                 Winner
Snake	         Water	             Snake (snake drinks the water)
Water	         Gun	             Water (gun sinks in water)
Gun	             Snake	             Gun (gun defeats the snake)
Same choice	     Same choice	             Draw
'''

import random
# Computer's choice
computer = random.choice(['Snake', 'Water', 'Gun'])
# User's choice
user = input("Enter your choice (Snake, Water, Gun): ")
if computer == user:
    print("It's a tie!🤝")
# Computer wins
elif computer == "Snake" and user == "Water":
    print("You lost 💔")
    print("BETTER LUCK NEXT TIME")
elif computer == "Water" and user == "Gun":
    print("You lost 💔")
    print("BETTER LUCK NEXT TIME")
elif computer == "Gun" and user == "Snake":
    print("You lost 💔")
    print("BETTER LUCK NEXT TIME")
# User wins
elif computer == "Water" and user == "Snake":
    print("You Won 😊")
elif computer == "Gun" and user == "Water":
    print("You Won 😊")
elif computer == "Snake" and user == "Gun":
    print("You Won 😊")

else:
    print("Invalid input!")

print(f"Computer chose {computer}")