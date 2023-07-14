import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

number_list = []
for i in range(1, 101):
    number_list.append(i)
number = random.choice(number_list)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    print("You have 10 attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    while EASY_ATTEMPTS != 1 and guess != number:
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        EASY_ATTEMPTS -= 1
        print(f"Guess again. You have {EASY_ATTEMPTS} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}!")
    if EASY_ATTEMPTS == 1:
        print("You've run out of attempts. You lose.")
        print(f"The correct number was {number}.")

elif difficulty == "hard":
    print("You have 5 attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    while HARD_ATTEMPTS != 1 and guess != number:
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        HARD_ATTEMPTS -= 1
        print(f"Guess again. You have {HARD_ATTEMPTS} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}!")
    if HARD_ATTEMPTS == 1:
        print("You've run out of attempts. You lose.")
        print(f"The correct number was {number}.")