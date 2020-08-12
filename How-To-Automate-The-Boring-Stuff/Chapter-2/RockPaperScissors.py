# Rock, Paper, Scissors
# TODO: Add a game loop, finish off conditionals.
# TODO: Add error handling COMPLETED
# TODO: Look at how to use less code from coding example

import random
import sys

wins = 0
losses = 0
ties = 0

print("ROCK, PAPER, SCISSORS")

while True:

    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))

    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")

        choice = input()

        # I can add "or" statements to make the code cleaner
        if choice == "r":
            print("ROCK versus...")
            break
        elif choice == "p":
            print("PAPER versus...")
            break
        elif choice == "s":
            print("SCISSORS versus...")
            break
        elif choice == "q":
            sys.exit()
        else:
            print("Please type one of r, p, s, or q")

    computerChoice = random.randint(1, 3)

    if computerChoice == 1:
        print("ROCK")
    elif computerChoice == 2:
        print("PAPER")
    elif computerChoice == 3:
        print("SCISSORS")

    if choice == "r":
        if computerChoice == 1:
            print("It is a tie!")
            ties += 1
        elif computerChoice == 2:
            print("You lose")
            losses += 1
        elif computerChoice == 3:
            print("You win!")
            wins += 1
    elif choice == "p":
        if computerChoice == 1:
            print("You win!")
            wins += 1
        elif computerChoice == 2:
            print("You tie!")
            ties += 1
        elif computerChoice == 3:
            print("You lose!")
            losses += 1
    elif choice == "s":
        if computerChoice == 1:
            print("You lose!")
            losses += 1
        elif computerChoice == 2:
            print("You win!")
            wins += 1
        elif computerChoice == 3:
            print("You tie!")
            ties += 1

# this is a cleaner version of the code:
print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break  # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1

# SUMMARY:
# Using boolean expression also the program to make decisions on what code
# to execute.
# break and continue statements are useful for exiting or jumping back to the top
# of a loop
