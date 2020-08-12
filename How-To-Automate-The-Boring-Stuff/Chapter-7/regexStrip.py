# Regex version of the strip() method

import re

# Write a function that takes a string and does the same thing as the strip() string method.
# If no other arguments are passed other than the string to strip, then whitespace characters
# will be removed from the beginning and end of the string. Otherwise, the characters specified
# in the second argument to the function will be removed.

# NOTE: My original plan didn't work so I revised as I went along. I need to learn to plan better.
# TODO: add a way to strip the string, without passing any arguments except for the string to strip.
# NOTE: the solution is pass a tuple, or a list as a single argument to. The list will either have 1 or 2 items.


def stripRegex(strippedChar, string):

    # We need to seperate characters and store them in order to pattern match individual characters.
    indivStringList = []
    for char in aChar:
        indivStringList.append(char)

    # Then we iteraite over the string parameter and keep track of every new string we create.
    # NOTE: Strings are immutable so we need to create a new string every time we replace characters.
    #       This is why we have a list to hold each iteration. We can replace just index 0 but I want to see all iterations of the string we create.
    newString = [string]

    # This will pattern match each char we stored and take any char's out of the newest iteraion of the original string we want to search.
    index = 0
    for item in indivStringList:
        regex = re.compile(item)
        mo = regex.search(newString[index])
        # NOTE: mo = ... will not hold a returnable value.
        #       If we find a match, we use the .group() method to return the match object and covert to a string. The "mo string" is used to replace characters.
        if mo != None:
            char = str(mo.group())
            replacedChar = newString[index].replace(char, "")
            newString.append(replacedChar)
        index += 1

    # In order to strip whitespaces from both left and right we need get the first and last chars in the replaced string.
    # Then we need to splice the string between those indices and print the final string.
    firstLetter = ""
    lastLetter = ""

    for char in newString[-1]:
        if char != " ":
            firstLetter = char
            break

    for i in range((len(newString[-1]) - 1), 0, -1):
        if newString[-1][i] != " ":
            lastLetter = newString[-1][i]
            break

    firstLetterIndex = newString[-1].find(firstLetter)
    # NOTE: rindex() will return the last occurence of the char/str passed. This is very useful.
    lastLetterIndex = newString[-1].rindex(lastLetter)

    stripedString = newString[-1][firstLetterIndex:(lastLetterIndex + 1)]
    print(stripedString)


# Overloading stripRegex to take only a single string to strip. Python does not support this however.
def stripRegex(string):

    firstLetter = ""
    lastLetter = ""

    for char in string:
        if char != " ":
            firstLetter = char
            break

    for i in range((len(string) - 1), 0, -1):
        if string[i] != " ":
            lastLetter = string[i]
            break

    firstLetterIndex = string.find(firstLetter)
    lastLetterIndex = string.rindex(lastLetter)

    stripedString = string[firstLetterIndex:(lastLetterIndex + 1)]
    print(stripedString)


aString = "   My name is Lucas   "
aChar = "Lucas"

#stripRegex(aChar, aString)
stripRegex(aString)
