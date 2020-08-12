# working with strings

# PART 1: STRNG LITERALS:
# strings begin and end with a pair of double of single quotes.

# Doubles Quotes:
# Using double quotes always use to use single quotes inside the string.
import pyperclip
spam = "That is Alice's cat."

# ESCAPE CHARACTERS:
# Escape characters lets me use characters that can't be put into a string.
# we use a "\" follsoed by that character I want.
spam = 'Say hi to bob\'s mother.'

# escape character || prints as
# \'               || single quotes
# \"               || double quotes
# \t               || tab
# \n               || newline
# \\               || backslash

print("Hello there!\nHow are you?\nI\'m doing fine.")

# RAW STRINGS:
# place an r before the beginning quotation mark of a string to make it a raw string.
# A raw string ignores all escape characters and prints any backslash that appears.
print(r"That is Carol\'s cat.")

# NOTE: Raw strings are useful if I'm typing a string value that contains multiple backslashes
# like a Windows file path r"User/User/desktop/python/chapter 5" or REGULAR EXPRESSIONS

# MULTILINE STRINGS WITH TRIPLE QUOTES:
# I can use \n for newline but, it's easier to use multiline strings.
# It starts with 3 single or double quotes. Any quotes, tabs, or newlines in between
# the triplets are part of the string.

print("""Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob""")

# MULTILINE COMMENTS:
# Hash "#" characters mark the beginning of a comment for the rest of the line.
# A multiline string is often used for coments that spam multiple lines.

"""This is a test Python program.
Written by Lucas del Villar superawesome@superawesome.

This program was designed for Python 3.
"""


def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print("Hello!")


spam()

# PART 2: INDEXING AND SLICING STRINGS:
# strings use indexes and slices the same way lists do. They use index 0 and -1 as well.
spam = "Hello, world!"
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[7:])

# NOTE: slicing a string does not modify the original string. You can store a slice in another
# variable
spam = "Hello, world!"
fizz = spam[0:5]
print(fizz)

# PART 3: THE IN AND NOT IN OPERATORS WITH STRINGS
# The "in" and "not in" operators can be used with strings just like with list values.
print("Hello" in "Hello, World")
print("Hello" in "Hello")
print("HELLO" in "Hello, World")
print("" in "spam")
print("cats" not in "cats and dogs")

# PUTTING STRINGS INSIDE OTHER STRINGS:
# Putting strings inside other strings is a common operation in programming.
# So far, we've used the "+" operator to concatenate strings.
name = "Al"
age = 4000
print("Hello, my name is " + name + ". I am " + str(age) + " years old.")

# However, this requires a lot of tedious typing. A simpler approach is to use string
# interpolation, which the % operator inside the string acts as a marker to be replaced
# by values following the string.
# NOTE: A benefit of string interpolation is that str() doesn't have to be called to convert
# values to strings.

name = "Al"
age = "4000"
print("My name is %s. I am %s years old." % (name, age))

# LOOK UP F-STRINGS - I DON'T WANT TO USE THIS. I PREFER %S

# USEFUL STRING METHODS
# PART 4: THE UPPER(), LOWER(), ISUPPER(), ISLOWER() METHODS

# upper() and lower() return a new string where all the letters in the original string
# are upper or lowercase.

spam = "Hello, world!"
spam = spam.upper()
print(spam)

spam = spam.lower()
print(spam)

# NOTE: the methods do not change the string. They return a new string value. This
# is why you need to "re-store" what upper() and lower() return.
# using:
spam.upper()
# won't change anything. It's like typing
1
# you need to assign the new value to be used later on.

# These methods are useful if you need to make a case-INSENSITIVE comparison.
print("How are you?")
feeling = input()

if feeling.lower() == "great":
    print("I feel great too.")
else:
    print("I hope the rest of your day is good.")

# The isupper() and islower() methods return a Boolean value.
spam = "Hello, world!"
print(spam.islower())
print(spam.isupper())
print("HELLO".isupper())
print("abc12345".islower())
print("12345".islower())
print("12345".isupper())

# since upper() and lower() return strings, you can call string methods on those returned
# string values as well.

print("Hello".upper())
print("Hello".upper().lower())
print("Hello".upper().lower().upper())
print("HELLO".lower())
print("HELLO".lower().islower())

# PART 5: THE ISX() METHOD
# The are many other methods that have names beginning with the word is that return
# boolean values. Look up what they below do:

print("hello".isalpha())  # returns true if the string consists of only letters and isn't blank
print("hello123".isalpha())

# returns true if the string consists of only letters and numbers and not blank
print("hello123".isalnum())
print("hello".isalnum())

print("123".isdecimal())  # returns true if the string consists only of numeric characters and is not blank
print("   ".isspace())  # returns true if the string consists only of words that begin with an uppercase
# returns true if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
print("This Is Title Case".istitle())
print("This Is Title Case 123".istitle())
print("This Is not Title Case".istitle())
print("This Is NOT Title Case Either".istitle())

# NOTE: this isX() methods are useful when you need to validate user input.
# see validate.py

# PART 6: THE STARTSWITH() AND ENDSWITH() METHODS
# returns true if the string value they are called on begins or ends with
# the string passed to the method.

print("Hello, world!".startswith("Hello"))
print('Hello, world!'.endswith('world!'))
print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12'))
print('Hello, world!'.startswith('Hello, world!'))
print('Hello, world!'.endswith('Hello, world!'))

# NOTE: useful alternatives to the == operator if you need to check only wheter
# the first or last part of the string, rather than the whole thing, is equal to another string.

# PART 7: THE JOIN() AND SPLIT() METHODS
# join() is used to join together a list of strings into a single string value.

print(", ".join(["cats", "rats", "bats"]))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))

# The split method does the opposite.

print("My name is Simon".split())

# You can use a delimiter string to split() to use different string to split upon.
print("MyABCnameABCisABCSimon".split("ABC"))
print('My name is Simon'.split('m'))

# NOTE: A common use of split() is to split a multiline string along the newline characters.

spam = """Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob"""

print(spam.split("\n"))

# passing split() the argument "\n" lets us split the multiline string store in spam
# along the newlines and return a list in which each item corresponds to one line of the string.

# PART 8: SPLITTING STRINGS WITH PARTITION() METHOD
# partition() string method can split a string into the text before and after a separator string.
# it seaches the string it is called on for the separator string it is passed and returns a tuple of
# three substrings for the "before", "separator", "after".

print('Hello, world!'.partition('w'))
print('Hello, world!'.partition('world'))

# if the separator string occurs multiple times partition() splits the string
# only on the first occurrence.

# if the separator string can't be found, the first string returned will be the entire string,
# and the other two strings will be empty.

# NOTE: you can use the multiple assignment trick to assign the three returned strings to three variables.
before, sep, after = "Hello, world!".partition(" ")
print(before)
print(after)

# NOTE: thie method is useful for splitting a string whenever you need the parts before,
# including, and after a particular separator string.

# PART 9: JUSTIFYING TEXT WITH THE RJUST(), LJUST(), AND CENTER() METHODS
# rjust() and ljust() return padded versions of the string they are called on, with
# spaces inserted to justify the text.

print("Hello".rjust(10))
print("Hello".rjust(20))
print("Hello, World".rjust(10))
print("Hello".ljust(10))

# there is an optional argument to both rjust() and ljust().

print("Hello".rjust(20, '*'))
print("Hello".ljust(20, '-'))

# the center() string works the same as ljust() and rjust().

print("Hello".center(20))
print("Hello".center(20, '='))

# NOTE: These methods are useful when you need to print tabular data that has correct spacing.
# please see picnicTable.py

# NOTE: the string will fill as many justified spaces as possible before the remaining justified spaces or other
# paramter string given appears. e.g. for "Hello".rjust(10)  "hello" will fill 5 of the
# 10 justified spaces this 5 white spaces will appear on the left. Think of the function has moving the word to the right.

# PART 10: REMOVING WHITESPACE WITH THE STRIP(), RSTRIP(), AND LSTRIP()
# strip() returns a new string without any whitespaces at the beginning or end.
# lstrip() and rstrip() removes whitespaces from either the left or right ends.

spam = '    Hello, World    '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

# optionally a string argument will specify which characters on the ends should be stripped.

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

# PART 11: NUMBERIC VALUES OF CHARACTERS WITH THE ORD() AND CHR() FUNCTIONS
# We need to be able to convert text to numbers. Every text character has a numeric value called
# a Unicode code point. ord() gets the code point of one-character string,
# and chr() gets the one-character string of an integer code point

print(ord('A'))
print(ord('4'))
print(ord('!'))
print(chr(65))

# NOTE: useful when you need to do an ordering or mathematical operation on characters.

print(ord('B'))
print(ord('A') < ord('B'))
print(chr(ord('A')))
print(chr(ord('A') + 1))

# PART 12: COPYING AND PASTING STRINGS WITH THE PYPERCLIP MODULE
# pyperclip module has copy() and paste() that can send text to and receive text
# from you computer's clipboard.
# Sending the output of your program to the clipboard will make it easy to paste it into an email
# word processor, or other software.

# import pyperclip
pyperclip.copy("Hello, world!")
print(pyperclip.paste())
