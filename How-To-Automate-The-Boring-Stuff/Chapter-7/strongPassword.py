# Strong Password Detection

import re

# Write a function that uses regex to make sure the password string it is passed is strong.
# A strong password is defined as one that is at least eight characters long, contains both
# uppercase and lowercase characters, and has at least one digit. You may need to test the
# string against multiple regex patterns to validate its strength.


def strongPassword(string):
    eightCharRegex = re.compile(r"[a-zA-Z0-9]{8,}")
    oneUpperRegex = re.compile(r"\W+")
    oneLowerRegex = re.compile(r"\w+")
    oneDigitRegex = re.compile(r"\d+")

    if eightCharRegex.search(string) != None:
        if oneUpperRegex.search(string) != None:
            if oneLowerRegex.search(string) != None:
                if oneDigitRegex.search(string) != None:
                    print("Password is strong")
                else:
                    print("Password is not strong")
            else:
                print("Password is not strong")
        else:
            print("Password is not strong")
    else:
        print("Password is not strong")


# TODO: create a regex for 8 characters long
    # [a-zA-Z0-9]{8}+
# TODO: create a regex for at least one upper case characters
    # \W+
# TODO; create a regex for at least one lower case character
    # \w+
# TODO: create a regex for at least one digit
    # \d+

# TODO: create test cases for each

testOne = "Lorenzo1"            # valid
testTwo = "lorenzo1"            # upper case test
testThree = "LORENZO1"          # lower case test
testFour = ""
testFive = ""
testSix = ""
testSeven = ""
testEight = ""
testNine = ""
testTen = ""

testCases = []


strongPassword(testOne)
