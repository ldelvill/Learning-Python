# The Collatz Sequence


def collatz(number):
    if (number % 2) == 0:                       # checks if number is even
        number = number // 2
    else:                                       # else it's odd
        number = 3 * number + 1

    return number


print("Enter a positive number:")

try:
    userNumber = int(input())                   # gets user input as an int

    if userNumber > 0:                          # checks if userNumber is positive
        while (userNumber != 1):                # lets computer call collatz() repeadtly
            userNumber = collatz(userNumber)
            print(userNumber)
except (ValueError, NameError):                 # potentially errors to be handled
    print("Please enter a positive integer.")
