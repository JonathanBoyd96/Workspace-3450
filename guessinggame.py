#guessinggame.py
import random
the_number = random.randint(1,10)
guess = int(input("Guess a number from 1 to 10: "))
while guess != the_number:
    if guess < the_number:
        print(guess, "was too low. Try again.")
    if guess > the_number:
        print(str(guess) + "was too high. Try again.")
    guess = int(input("Guess a number from 1 to 10: "))
print("Guess was the right number! You win!")
