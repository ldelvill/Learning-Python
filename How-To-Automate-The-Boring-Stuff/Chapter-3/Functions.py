# FUNCTIONS
# A function lets you recall previously written code.

import random


def hello():
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")


hello()

# avoid duplicating code, because if I need to
# update my code, it'll be easier to change

# PART 2: def STATEMENTS WITH PARAMETERS
# when calling functions you pass ARGUMENTS in the paratheses.
# you can also define your own functions that have ARGUMENTS


def hello(name):
    print("Hello," + name)


hello("Alice")
hello("Bob")

# the definition of hello(name) has a PARAMETER called name.
# parameters are variables that hold ARGUMENTS
# NOTE: values stored in parameters are forgetten when the function
# returns.

# PART 3: DEFINE, CALL, PASS, ARGUMENT, PARAMETER


def sayHello(name):
    print("Hello," + name)


sayHello("Al")

# to def a function is to create it. When you use the function you call it.
# You pass a value into a function. The passes value is called the argument.
# The parameter is what holds the passed value, i.e. argument.

# RETURN VALUES AND RETURN STATEMENTS
# The value that a function evaluates to is called the return value.
# you can "keep" the value by using a return statement.

# import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidely so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My repy is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"


r = random.randint(1, 9)
fortune = getAnswer(r)

print(fortune)

# PART 4: THE NONE VALUES
# None represents the absence of a value.
# Helpful if you need to store something that won't be confused
# for a real value in a variable.
# The print function returns None. You don't need to specify returning
# None in python. Some programming languages you do.

spam = print("Hello!")
print(None == spam)  # will be True

# PART 5: KEYWORD ARGUMENTS AND THE PRINT() FUNCTION
# Most arguments are identified by their position in the function call.
# random. randint(1, 10) is different from random.randint(10,1).
# The latter will cause an error.
# KEYWORD ARGUMENTS are identified by the keyword put before them in a
# function call. Keyword arguments are used for optional parameters.
# print() has the optional parameters end and sep to specify what should
# be printed at the end of its arguments and between its arguments.

print("Hello")
print("World")

# the above prints on a newline, because the print function automatically adds
# a newline character. If I want to ignore that then do the following.

print("Hello", end="")
print("World")

print("cats", "dogs", "mice")
print("cats", "dogs", "mice", sep=",")  # this replaces the space with a comma.

# You can add keyword arguments to functions you write but that will be covered
# in a later chapter. For now some functions have optional keyword arguments.

# PART 6: THE CALL STACK
# Python will remember which line of code called the function so that
# the execution can return a value when it encounters a return statement.
# If the original function calls another function, the execution will return
# those function calls first, before returning from the original function call.
# this is called the stack. The current call will always be at the top of the stack.
# See below to better understand.


def a():
    print("a() starts")
    b()
    d()
    print("a() returns")


def b():
    print("b() starts")
    c()
    print("b() returns")


def c():
    print("c() starts")
    print("c() returns")


def d():
    print("d() starts")
    print("d() returns")


a()

# the call stack is how Python remembers where to return the
# execution afer each function call. When my program calls a function
# Python creates a frame object on the top of the call stack.
# Frame objects store the line number of the original function call
# so that Python can remember where to return. If another function call
# is made, Python puts another frame object on the call stack above the other one.
# When a function call returns, Python removes a frame object from the top of the stack,
# and moves the execution to the line number where it was called.
# NOTE: frame objects are always removed from the top of the stack.

# PART 7: LOCAL AND GLOBAL SCOPE
# Parameters and variables are in a function's local scope (local variables).
# Anything outside are set in a global scope (global variables).
# Local variables are only remembered within the function. The variables get
# destroyed once the execution of the local and global scope ends.
# NOTE: local variables are also stored in the frame object.
# it is a bad habit to rely on global variables as my programs get longer.

# Local variables can't be used in the global scope:


def spam():
    eggs = 31337


spam()
# print(eggs) eggs doesn't exist and I get an error.

# Local scopes can't use variables in other local scopes:


def spam():
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs = 0


spam()

# Global variables can be read from a local scopes


def spam():
    print(eggs)


eggs = 42
spam()
print(eggs)

# Local and global variables with the same name:


def spam():
    eggs = "spam local"
    print(eggs)


def bacon():
    eggs = "bacon local"
    print(eggs)
    spam()
    print(eggs)


eggs = "global"
bacon()
print(eggs)

# PART 8: THE GLOBAL STATEMENT
# If I need to modify a global variable within a function, use the global statement
# It tells Python to not create a local variable called eggs. But use the global
# variable eggs.


def spam():
    global eggs
    eggs = "spam"


eggs = "global"
spam()
print(eggs)

# to further solidify concept:


def spam():
    global eggs
    eggs = "spam"


def bacon():
    eggs = "bacon"


def ham():
    print(eggs)


eggs = 42
spam()
print(eggs)


# NOTE:FUNCTIONS AS "BLACK BOXES"
# Often we only need to know about a functions inputs and output value,
# we don't always need to know how the functions code always works.
# This is called treating a function like a "black box".

# Part 9: Exception Handling
# Errors can be handled with try and except statements. The code that
# can potentially have an error is put in a try clause. The program
# execution moves to the start of a following except clause if an error happens.
# And execution continues as normal.


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# SUMMARY:
# Functions are the primary way to compartmentalize code. Local variables
# cannot effect anything outside their scope. This limits what code could be
# changing my values. You can think of function like black boxes.

# PRACTICE QUESTIONS:
# 1. Why are functions advantageous to have in your program?
