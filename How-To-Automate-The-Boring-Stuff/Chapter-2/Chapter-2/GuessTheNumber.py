# Guess the number game.
# User has to pick a number between 1 and 20

import random

number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

count = 0
while True:
    print("Take a guess.")
    guess = int(input())

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    elif guess == number:
        count += 1
        break

    count += 1

print("Good job! You guessed my number in " + str(count) + " guesses.")
