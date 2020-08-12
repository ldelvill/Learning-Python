import pyinputplus as pyip
# Input validation code checks that values entered by the user, such as text from the input()
# function, are formatted correctly. If you want users to enter their ages, your code shouldn't
# accept nonsensical answers such as negative numbers or words. Input validation can also
# prevent bugs or security vulnerabilites. If you implement a withdrawFromAccount() function
# that takes an argument for the amount to subtract from an account, you need to ensure the amount
# is a positive number. If the withdrawFromAccount() function subtracts a negative number from the
# account, the "withdrawal" will end up adding money!

# Typically we perform input validation by repeatedly asking the user for input until they enter
# valid text, as in the following.

while True:
    print("Enter you age:")
    age = input()
    try:
        age = int(age)
    except:
        print("Please use numeric digits.")
        continue
    if age < 1:
        print("Please enter a positive number.")
        continue
    break

print(f"Your age is {age}.")

# When you run this code, you'll be prompted for your age until you enter a valid one.
# This ensures that by the time the execution leaves the while loop, the age variable will
# contain a valid value that won't crash the program later on.

# However, writing input validation code for every input() call in you program quickly becomes tedious.
# Also, you may miss certain cases adn allow invalid input to pass through your checks. In this chapter,
# you'll learn how to use the third-party PyInputPlus module for input validation.


# PART 1: THE PYINPUTPLUS MODULE


# PyInputPlus contains functions similar to input() for several kinds of data: numbers, dates, email addresses,
# and more. If the user enters invalid input, such as a badly formatted date or a number that is outside of an
# intended range, PyInputPlus will reprompt them for input just like our code in the previous section did.
# PyInputPlus lso has other useful features like a limit for the number of times it reprompts users and a timeout
# if users are required to respond within a time limit.

# PyInputPlus is not part of the Python Standard Library, so you must install it separately using pip. Follow install
# instructions in book.

# PyInputPlus has several functions for different kinds of input:

# inputStr() - Similar to the built in input() function but has the gernarl PyInputPlus features.
# You can also pass a custom validation function to it.

# inputNum() - Ensures the user enters a number and returns an int or float, depending on if the number
# has a decimal point in it.

# inputChoice() - Ensures the user enters on of the provided choices.

# inputMenu() - Is similar to inputChoice(), but provides a menu with numbered or lettered options.

# inputDatetime() - Ensures the user enters a date and time.

# inputYesNo() - Ensures the user enters a "yes" or "no" response.

# inputBool() - Is similar to inputYesNo(), but takes a "True" or "False" response and returns a Boolean value.

# inputEmail() - Ensures the user enters a valid email address.

# inputFilepath() - Ensure the user enters a valid file path and filename, and can optionally check that a file with
# that name exists.

# inputPassword() - Is like the built-in input(), but display * charactesr as the user types so that passwords,
# or other sensitive information, aren't displayed on the screen.

# NOTE: These functions will automatically reprompt the user for as long as they enter invalid input:

# import pyinputplus as pyip
print("Please enter a number: ")
response = pyip.inputNum()
print(response)

# The as pyip code in the import statement saves us from typing pyinputplus each time we want to call
# a PyInputPlus function. Instead we can use the shorter pyip name.
# NOTE: If you take a look at the example, you see that unlike input(), these functions return an int or float value:
# 42 and 3.14 instead of the string "42" and "3.14".

# Just as you can pass a string to input() to proivde a prompt, you can pass a string to a PyInputPlus functions's
# prompt keyword argument to display a prompt:

response = input("Enter a number: ")
print(response)

response = pyip.inputInt(prompt="Enter a number: ")
print(response)

# NOTE: Use Python's help() function to find out more about each of these functions. For example,
# help(pyip.inputChoice) displays help information for the inputChoice() function.
# Complete documenation can be found at https://pyinputplus.readthedocs.io/.

# Unlike Python's built-in input(), PyInputPlus functions have several additional features for input validation.


# THE MIN, MAX, GREATERTHAN, AND LESSTHAN KEYWORD ARGUMENTS:


# The inputNum(), inputInt(), and inputFloat() functions, which accept int and float numbers, also have min, max,
# greaterThan, and lessThan keyword arguments for specifying a range of valid values. For example,
# enter the following into the interactive shell:

print("Enter a num at minimum 4")
response = pyip.inputNum("Enter num: ", min=4)
print(response)
print("Enter a num > 4")
response = pyip.inputNum("Enter num: ", greaterThan=4)
print(response)
print("Enter a num >= 4 and < 6")
response = pyip.inputNum(">", min=4, lessThan=6)
print(response)

# These keyword arguments are optional, but if supplied, the input cannot be less than the min argument or
# greater than the max argument (though the input can be equal to them).
# Also, the input must be greater than the greaterThan and less than the lessThan arguments
# (that is, the input cannot be equal to them).


# THE BLANK KEYWORD ARGUMENT:


# By default, blank input isn't allowed unless the blank keyword argument is set to True:
print(" If you enter nothing. You will have to try again.")
response = pyip.inputNum("Enter num: ")
print(response)
print("Enter nothing this time. It will work.")
response = pyip.inputNum(blank=True)
print(response)

# NOTE: Use blank = True if you'd like to make input optional so that the user doesn't need to enter anything.


# THE LIMIT, TIMEOUT, AND DEFAULT KEYWORD ARGUMENTS:

# If you'd like a function to stop asking the user for input after a certain number of tries or a certain
# amount of time, you can use the limit and timeout keyword arguments. Pass an integer for the limit keyword
# argument to determine how many attemps a PyInputPlus function will make to receive valid input before giving up,
# and pass an integer for the timeout keyword argurment to determine how many seconds the user has to enter
# valid input before the PyInputPlus function gives up.

# If the user fails to enter valid input, these keyword arguments will cause the function to raise a
# RetryLimitException or TimeoutException, respectively. For example, enter the following:

print("Enter anything but a number twice.")
response = pyip.inputNum(limit=2)
print("Wait 10s and then enter.")
response = pyip.inputNum(timeout=10)

# When you use the keyboard arguments and also pass a default keyword argument, the function returns the default value
# instead of raising an exception. Enter the following.

print("Enter anything but a number:")
response = pyip.inputNum(limit=2, default="N/A")

# Instead of raising RetryLimitException, the inputNum() function simply returns the string "N/A".


# THE ALLOWREGEX AND BLOCKREGEXES KEYWORD ARGUMENTS:
# You can also use regex to specify wheter an input is allowed or not. The allowRegexes and blockRegexes keyword
# arguments take a list of regex strings to determine what the PyInputPlus function will accept or
# regect as valid input. For example, enter the following code into the interactive shell so that
# inputNum() will accept Roman numerals in addition to the usual numbers:

print("Enter any of the following: I, V, X, L, C, D, M.")
response = pyip.inputNum(allowRegexes=[r"(I|V|X|L|C|D|M)+", r"zero"])
print(response)

print("Enter any of the following: i, v, x, l, d, d, m.")
response = pyip.inputNum(allowRegexes=[r"(i|v|x|l|c|d|m)+", r"zero"])

# Of course, this regex affects only what letters the inputNum() function will accept from
# the user; the function will still accept Roman numerals with invalid ordering such as "XVX" or "MILLI"
# because the r"(I|V|X|L|C|D|M)+" regex accept those strings.

# You can also specify a list of regex strings that a PyInputPlus Function won't accept by using the blockRegexes
# keyword argument. Enter the following into the interactive shell so that inputNum() won't accept even numbers:


print("Enter any of the following and it won't be allowed: 0, 2, 4, 6, 8")
response = pyip.inputNum(blockRegexes=[r"[02468]$"])
print(response)

# if you specify both an allowRegexes and blockRegexes argument, the allow list overrides the block list.
# For example, enter the following into the interactive shell, which allows "caterpillar" and "category"
# but blocks anything else that has the word "cat" in it:

print("Enter caterpillar or category. Anything else or anything with cat will not work.")
response = pyip.inputStr(allowRegexes=[r"caterpillar", "category"], blockRegexes=[r"cat"])
print(response)

# The PyInputPlus module's functions can save you from writing tedious input validation code yoursel.
# But there's more to the PyInputPlus module than what has been detailed here. You can examine its full
# documentation online at https://pyinputplus.readthedocs.io/.


# PASSING A CUSTOM VALIDATION FUNCTION TO INPUTCUSTOM():


# You can write a function to perform your own custom validation logic by passing the function to inputCustom().
# For example, say you want the user to enter a series of digits that adds up to 10. There is no pyinputplus.inputAddsdUpToTen()
# function, but you can create your own one that:

# - Accepts a single string argument of what the user entered
# - Raises an exception if the string fails validation
# - Returns None (or has no return statement) if inputCustom() should return the string unchanged.
# - Returns a non-None value if inputCustome() should return a different string from the one the user entered
# - Is passed as the first argument to inputCustom(), not calling addsUpToTen() and passing its return value.

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception("The digits must add up to 10, not %s." % (sum(numbersList)))
    return int(numbers)


print("Enter numbers that add up to ten.")
response = pyip.inputCustom(addsUpToTen)
print(response)


# PROJECT: HOW TO KEEP AN IDIOT BUSY FOR HOURS
# go to chapterEightProject.py


# It's easy to forget to write input validation code, but without it, your programs will
# almost certainly have bugs. The values you expect users to enter and the values they actually
# enter can be completely different, and your programs need to be robust enough to handle these
# exceptional cases. You can use regex to create your own input validation code,
# but for common cases, it's easier to use an existing module, such as PyInputPlus.
# You can import the module with import pyinputplus as pyip so that you can enter a shorter name
# when calling the module's functions.

# PyInputPlus has functions for entering a variety of input, including strings, numbers, dates, yes/no,
# True/False, emails, and files. While input() always returns a string, these functions return the value in
# in an appropriate data type. The inputChoice() function allows you to select one of several
# pre-selected options, while inputMenu() also adds numbers or letters for quick selection.

# NOTE: All of these functions have the following standard features: stripping whitespace from the sides,
# setting timeout and retry limits with the timeout and limit keyword arguments, and passing lists of
# regex strings to allowRegexes or blockRegexes to include or exclude particular responses. You'll
# no longer need to write your own tedious while loops that check for valid input and repromprt the user.

# If none of the PyInputPlus module's, functions fit your needs, but you'd still like the other features that
# PyInput provides, you can call inputCustom() and pass your own custome validation function for
# PyInputPlus to use. The documeentation at https://pyinputplus.readthedocs.io/en/latest/ has a complete
# listing of PyInputPlus's functions and additional features. There's far more in the PyInputPlus online
# documentation that what was described in this chapter. There's no use in reinventing the wheel,
# and learning to use this module will save you from having to write and debug code for yourself.

# Now that you have expertise in manipulating and validating text, it's time to learn how to read
# from and write to files on your computer's hard drive.


# PRACTICE QUESTIONS:

# 1. Does PyInputPlus come with Python Standard Library?
# No it does not. You need to install it using the pip command.

# 2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?
# it makes it eaiser to type methods.

# 3. What is the difference between inputInt() and inputFloat()?
# inputInt() will only accept ints, and inputFloat() will only accept floating point numbers.

# 4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?
# create my own function to validate input then pass it through pyip.inputCustom().

# 5. What is passed to the allowRegexes and blockRegexes keyword arguments?
# regexes that you will allow or regexes that you want to block

# 6. What does inputStr(limit=3) do if blank input is entered three times?
# It will raise an exception after 3 invalid inputs.

# 7. What does inputStr(limit=3, default="hello") do if blank input is entered three times?
# It will not raise an exception but return "hello" after 3 invalid tries.


# PROJECT: SANDWHICH MAKER
# please see sandwhichMaker.py


# PROJECT: WRITE YOUR OWN MULTIPLICATION QUIZ
# please see multiplicationQuiz2.py
