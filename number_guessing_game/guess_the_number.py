import art
import random


print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")
attempt = 10
game_over = False

while not game_over:
    if attempt != 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if number < guess:
            print("Too high.")
        elif number > guess:
            print("Too low.")
        else:
            print(f"You got it! The answer was {number}")
            game_over = True
    else :
        print("You've run out of guesses, you lose.")
        print(f"The correct answer was {number}")
        game_over = True
    attempt -= 1