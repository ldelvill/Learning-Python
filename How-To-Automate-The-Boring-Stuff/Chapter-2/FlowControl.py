# CHAPTER 2: FLOW CONTROL

# Flow control statements help decide which lines of code to execute
# under certain conditions

# Flow control diagram:
# rounded rectangles = start and end points
# diamonds = branching points, e.g. yes or no points
# other steps = rectangles

# PART 1: BOOLEAN VALUES

# Boolean data type has only two values, True or False.

import random
import math
import sys
import os
spam = True
print(spam)

# true # this gives an error message, supposed to be capital T

# PART 2: COMPARISON OPERATORS
# also called relational operators, compare two values and evaluate to a bool.

# Comparison Operators:
# ==        ||  equal to
# !=        ||  not equal to
# <         ||  less than
# >         ||  greater than
# <=        ||  less than or equal to
# >=        ||  greater than or equal to

print(42 == 42)  # True
print(42 == 99)  # False
print(2 != 3)   # True
print(2 != 2)   # False

# NOTE: == and = are different. Don't confuse that two.

# PART 3: BOOLEAN OPERATORS
# Three commonly used Boolean operators are: and, or, and not.
# Review truth tables in order to understand Boolean operators.

# PART 4: MIXING BOOLEAN AND COMPARISON OPERATORS
# You can mix both boolean and comparison operators since CO's evaluate to a bool.

print((4 < 5) and (5 < 6))  # True
print((4 < 5) and (9 < 6))  # False
print((1 == 2) or (2 == 2))  # True

# NOTE: There is an order of operations. After any math or compaison operator
# Python evaluates not, then and, then or.

# PART 5: ELEMENTS OF FLOW CONTROL
# Flow control statements are made up of conditions followed by a block of code called the clause.

# Boolean expressions are considered conditions (flow contrl statements).
# Conditions always evaluate down to a bool. A condition decides what to do based on the
# Boolean value.

# Blocks are made up of lines of indented code.

name = "Mary"
password = "swordfish"

if name == "Mary":
    print("Hello, Mary.")
    if password == "swordfish":
        print("Access granted.")
    else:
        print("Wrong password.")

# PART 6: FLOW CONTROL STATEMENTS
# if Statements:
# statement will execute if condition is True.
# NOTE: will always have a colon at the end

if name == "Alice":
    print("Hi, Alice.")

# else Statements:
# an if statment can be followed by an else statement.
# NOTE: will always have a colon at the indent.

if name == "Alice":
    print("Hi, Alice.")
else:
    print("Hello, stranger.")

# elif Statements:
# if we have multiple conditions to check we can use elif.
# At most one clause will be executed.
# NOTE: So elif is only executed if the preivous condition was false.
# NOTE: And we only want to use elif if we don't need to check all conditions.


name = "Alice"  # since first condition is true elif is skipped.
age = 11

if name == "Alice":
    print("Hi, Alice.")
elif age < 12:
    print("You are not Alice, kiddo.")

# More examples of elif statements:

print("\nVampire.py")

name = "Carol"
age = 3000

if name == "Alice":
    print("Hi, Alice")
elif age < 12:
    print("You are not Alice, kiddo.")
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire.")
elif age > 100:
    print("You are not Alice, grannie.")

# if we switch conditions for 2000 and 100 we get an error.
# we printed the wrong statement because 3000 > 100 but we wanted
# to print out the vampire string. elif skipped the clause because
# a previous condition was True.

print("\nLittleKid.py")

name = "Carol"
age = 3000

if name == "Alice":
    print("Hi, Alice")
elif age < 12:
    print("You are not Alice, kiddo.")
else:
    print("You are neither Alice nor a little kid.")

# in plain english: if the first condition is true do this. Else if, the second
# condition is true do that. Otherwise, do something else.

# while Loop Statements:
# while loops let you execute code over and over again.
# while loops will execute until the statement's condition is false.

spam = 0
if spam < 5:
    print("Hello, world.")
    spam = spam + 1

spam = 0
while spam < 5:
    print("Hello, world.")
    spam = spam + 1

# break Statements:
# a shortcut to break out of a while loop's block early is to use a break statement.

while True:
    print("Please type your name.")
    name = input()

    if name == "your name":
        break

    print("Thank you!")

# continue Statements:
# a shortcut to jump back to the loop condition

print("\nswordfish.py")

while True:
    print("Who are you?")
    name = input()

    if name != "Joe":
        continue
    print("Hello, Joe. What is the password? (It is a fish.)")

    password = input()
    if password == "swordfish":
        break

    print("Acess granted.")

# for loops and the range() function:
# used to execute a block of code a certain number of times
# used with the range() function

print("My name is")
for i in range(5):
    print("Jimmy Five Times (" + str(i) + ")")

# I can use break and continue statements in for loops

# Another example:

total = 0
for num in range(101):
    total = total + num
print(total)

# you can use a while loop to do the same thing as a for loops

print("My name is")
i = 0
while i < 5:
    print("Jimmy Five Times (" + str(i) + ")")
    i = i + 1

# starting, stopping, stepping arguments to range()

# certain functions can have multiple arguments seperate by commas.

for i in range(12, 16):
    print(i)

# third argument will let me know how many numbers to skipped

for i in range(0, 10, 2):
    print(i)

# negative numbers can be used to count down
for i in range(5, -1, -1):
    print(i)


# PART 7: IMPORTING MODULES

# python has modules (sets of related functions) called the standard library. Each
# much be imported using an import statement before being used.
# once you import a module you can use its functions

for i in range(5):
    print(random.randint(1, 10))


# important statement importing 4 modules:
# look at top of code
# impot random, sys, os, math also works

# NOTE: using from random import * lets my use all the functions
# in random but without the random.prefix

# PART 8: ENDING A PROGRAM EARLY WITH THE SYS.EXIT() function

# sys.exit() lets you terminate the program.

# import sys is at top of code

while True:
    print("Type exit to exit.")
    response = input()

    if response == "exit":
        sys.exit()

    print("You typed " + response + ".")
