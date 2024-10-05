import random

number_to_guess = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number_to_guess:
    print("Congratulations! You guessed it right.")
else:
    print(f"Sorry, the correct number was {number_to_guess}.")