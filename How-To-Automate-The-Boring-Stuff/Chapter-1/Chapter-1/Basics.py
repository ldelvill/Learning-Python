# PART 1: EXPRESSIONS
# The following is an example of an expression.
# Expressions consists of values and operators that reduce to a single value.

print(2 + 2)

# This evaluates to 4.
# Note: A single value is also considered an expression.

# List of other expressions:
# Exponent                          || 2 ** 3       || 8
# Modules                           || 22 % 8       || 6
# Integer division/floored quotient || 22 // 8      || 2
# Division                          || 22 / 8       || 2.75
# Multiplication                    || 3 * 5        || 15
# Subtraction                       || 5 - 2        || 3
# Addition                          || 2 + 2        || 4

# Note: Order of operations is followed as in math.

print(2 + 3 * 6)
print((2 + 3) * 6)
print(48565878 * 578453)
print(2 ** 8)
print(23 / 7)
print(23 // 7)
print(23 % 7)
print(2 + 2)
print((5 - 1) * ((7 + 1) / (3 - 1)))

# PART 2: DATA TYPES
# A data type is a category for values.

# Common Data Types:
# Integers                      || -2, -1, 0, 1
# Floating Point Numbers        || -1.25, -1.0, -0.5
# Strings                       || "Hellow World"

# PART 3: STRING CONCATENATION AND REPLICATION
# The addition operator "+" will join strings together i.e. concatenate.

print("Alice" + "Bob")

# Note: You can't add a string and an integer.
# print("Alice" + 42)

# The multiplication operator "*" will replicate a strings.
print("Alice" * 5)

# Note: You can't replicat a string with another string.
# print("Alice" * "Bob")

# PART 3: VARIABLES
# A variable holds a value. It is stored somewhere in the computers memory.
# If you want to save a result of an expression, store it as a variale to use later.
# The following is an example of an assignment statement. An assignment statement
# lets you hold a value in a variable.

spam = 40
print(spam)

eggs = 2
print(eggs)

print(spam + eggs + spam)

spam = spam + 2
print(spam)

# a variable is initialized (created) the first time a value is stored.
# It can be repeatedly used afterwards. When a new value is assigned, the
# old value is forgotten. This is called overwriting.

spam = "Hello"
print(spam)

spam = "Goodbye"
print(spam)

# PART 4: VARIABLE NAMES
# A good variable name describes the data it contains.

# Valid variable names:
# current_balance
# currentBalance
# account4
# TOTAL_SUM
# hello

# hyphens, spaces, variables starting with numbers, and special characters are
# not allowed.

# Variable names are case sensitive, i.e. spam and SPAM are different.
# NOTE: use camel case to name variables e.g. camelCase

print()  # instead of using print("\n") to create a newline just type print().
print("Beginning of first program:\n")

print("Hello, world!")
print("What is your name?")

myName = input()
print("It is good to meet you, " + myName)

print("The length of your name is:")
print(len(myName))

print("What is your age?")

myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")

# PART 4: DISSECTING THE CODE
# "#" add allow you to lines called comments that the compiler igonres.

# print() is a function that lets you output a string to your screen.
# A string value gets passed into the print() function. A value being passed
# is called an argument.

# input() allows a user to type a string.
# The function evalutes what is typed into a string value.

# Line 103 is an example of concatenation with a variable.

# len() gets passed a string value and returns the number of characters
# in that string.

# print(len("hi ")), the length is 3. a whitespace is included.

# str(), int(), float() allow you to convert data types so that they can be
# used if the current data type is not acceptable for use
# in the last line of code, the age was a string, then convertated to an
# integer to do addition, and must be convereted back to a string
# in order to concatenate the strings.

# int() is useful if you need to floor a number

# NOTE: TEXT AND NUMBER EQUIVALENCE
print(42 == '42')  # false
print(42 == 42.0)  # true
print(42.0 == 0042.000)  # true
