'''
We are writing a program that generates a random number and asks the user to
guess it.
If the player's guess is higher than the actual number, the program displays “Lower
number please” .
Similarly, if the user's guess is too low, the program prints “Higher number please” .
When the user guesses the correct number, the program displays the number of
guesses the player used to arrive at the number.

'''

import random
n1=int(input("Enter the starting number of the range you want to play the game within: "))
n=int(input("Enter the last number of the range you want to play the game within:  "))
computer=random.randint(n1,n)
c=1
while True:
    user=int(input(f"Guess  a number from {n1} to {n} :  "))
    if computer==user:
        print("Yeah you got it right")
        break
    elif user>computer:
        print("Lower number please")
        
        
    elif user<computer:
        print("Higher number please")

    c+=1
        
    
print(f"The number of guesses you took is {c}")
   