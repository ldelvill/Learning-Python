import re


# PART 1: FINDING PATTERNS OF TEXT WITHOUT REGULAR EXPRESSIONS


# Lets say you want to find a phone number in a string. The pattern is 3 numbers, a hyphen
# 3 numbers, a hyphen, and 3 numbers, e.g. 123-456-7890

# Let's use the function below:


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print("Is 415-555-4242 a phone number?")
print(isPhoneNumber("415-555-4242"))
print("Is Moshi moshi a phone number?")
print(isPhoneNumber("Moshi moshi"))

# If you wanted to find a phone number within a larger string, you would have to add
# more code to find the phone number pattern.
# Please see isPhoneNumber.py and it's notes.


# PART 2: FINDING PATTERNS OF TEXT WITH REGULAR EXPRESSIONS


# The previous phone number-finding program works, but uses a lot of code to do
# something limited and it doesn't validate for other formats. You can add more code
# but there is an easier way to do this.

# Regular expression, called regexes for short, are descriptions for a pattern of text.
# For example, a "\d" in regex stand for a digit character - any single numberical
# from 0 to 9. The regex \d\d\d-\d\d\d-\d\d\d\d is used by Python to match the same
# text pattern the previous isPhoneNumber() function did. Any other string would not match
# \d\d\d-\d\d\d-\d\d\d\d.

# But regular expression can be much more sophisticated. For example, adding a 3 in braces
# ({3}) after a pattern is like saying, "Match this patter three times". So a shorter version
# would be \d{3}-\d{3}-\d{4} also matches the correct phone number format.


# CREATING REGEX OBJECTS:


# All regex functions in Python are in the re module.

# NOTE: import re

# Passing a string value representing your regular expression to re.compile() returns a Regex
# pattern object (or simply, a Regex object).

# To create a Regex object that matches the phone number pattern, enter the following
# into the interative shell.

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# Now the phoneNumRegex variable contains a Regex object


# MATCHING REGEX OBJECTS:


# A regex object's search() method searches the string it is passed for any matches to the
# regex. search() will return None if a pattern is not found.
# If there is a pattern, search() returns a Match object, which have a group()
# method that will return the actual matched text from the searched string.

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search("My number is 415-555-4242.")
print("Phone number found: " + mo.group())

# mo stands for Match object.
# We pass our pattern to re.compile() and store the resulting regex object in phoneNumRegex.
# We call search() on phoneNumRegex and pass search() the string we want to match for.
# The result is stored in mo.
# We know a match object will be return in this program. Since mo contains a Match object
# and not the null value None, we can call group() on mo to return the match.
# Writing mo.group() inside our print() function call displays the whole match, 415-555-4242.


# REVIEW OF REGULAR EXPRESSION MATCHING:


# 1. Import regex module with import re.
# 2. Create a regex object with the re.compile() function. (Remember to use a raw string.)
# NOTE: a raw strings are strings beginning with an r that treat blackslashes as a literal character instead of an
# escape sequence like \n. e.g. r"This is an escape sequence \n"
# 3. Pass the string you want to search into the Regex object's search() method. This returns a Match object
# 4. Call the Match object's group() method to return a string of the actual matched text.


# PART 3: MORE PATTERN MATCHING WITH REGULAR EXPRESSIONS


# This will cover more powerful pattern-matching capabilities.


# GROUPING WITH PARENTHESES:


# Say you want to separate the area code from the rest of the phone number.
# Adding parentheses will create groups n the regex (\d\d\d)-(\d\d\d\-\d\d\d\d).
# Then you can use the gruop() match object method to grab the matching text from just one group.

# The first set of parentheses in a regex string will be group 1. The second set will be group 2.
# By passing the integer 1 or 2 to the group() Match object method, you can grab different
# parts of the matched text. Passing 0 or nothing to the group() method will return the entire matched text.
# Enter the following into the interactive shell.

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("My number is 415-555-4242")
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

# NOTE: If you wouldl ike to retrieve all the gruops at once, use the groups() method -- note the plural form of the name
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# NOTE: Since mo.groups() returns a tuple of multiple values, you can use the
# multiple assignment trick to assign each value to a separate variable, as in the previous
# areaCode, mainNumber = mo.groups() line.

# Parentheses have a special meaning in regular expressions, but what do you do if you need to match
# a parenthesis in your text. For instance what if we need to match the area code with a set of parenthesis.
# In this case, you need to escape the ( and ) characters with a backslash.

phoneNumRegex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("My phone number is (415) 555-4242.")
print(mo.group(1))
print(mo.group(2))


# The \( and \) escape characters in the raw string passed to re.compile() will match actual parenthesis characters.
# In regular expressions, the following characters have special meanings:

# . ^ * + ? { } [ ] ( )

# if you want to detec these characters as part of your text pattern, you need to escape them with a backslash:

# \. \^ \* \+ \? \{ \} \[ \] \( \)

# Make sure to double-check that you haven't mistaken escaped parentheses \( and \_ for
# parenthese ( and ) in a regular expresssion. If you receive an error message about
# "missing )" or "unbalanced parenthesis," you may have forgotten to include the closing unescaped parenthesis for a
# group, like in this example.

# re.compile(r"(\(Parentheses\)") will cause an error.


# MATCHING MULTIPLE GRUOPS WITH THE PIPE:


# The | character is called a pipe. You can use it anywhere you want to match one of many expressions.
# For exmaple, the regular expression r"Batman|Tina Fey" will match either "Batman" or "Tina Fey"

# When both Batman and Tina Fey occur in the searched string, the first occurrence of matching text will
# be returned as the Match object.

heroRegex = re.compile(r"Batman|Tina Fey")
mo1 = heroRegex.search("Batman and Tina Fey")
print(mo1.group())
mo2 = heroRegex.search("Tina Fey and Batman")
print(mo2.group())

# NOTE: You can find all matching occurrences with the findall() method that's discussed in "The findall() Method" on
# page 171.

# Pipe can also be used to match one of several patterns as part of your regex. For example, say you wanted to match
# any of the strings "Batman", "Batmobile", "Batcopter", and "Batbat". Since all these strings start
# with Bat, it would be nice if you could specify that prefix only once. This can be done with parentheses. Enter
# the following into the interactive shell.

batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())
print(mo.group(1))

# The method call mo.group() returns the full matched text "Batmobile", while mo.group(1) return just
# the part of the matched text inside the first parentheses group, "mobile". By using the pipe character and
# grouping parentese, you can specify several alternative patterns you would like your regex to match.

# If you need to match an actual pipe character, escape it with backslash, like \|.


# OPTIONAL MATCHING WITH THE QUESTION MARK:


# Sometimes there is a pattern that you want to match only optionally. That is, the regex
# should find a match regardless of whether that bit of text is there. The ? character flags
# the gruop that preceds it as an optional part of the pattern. For example. enter the following into the
# interactive shell.

batRegex = re.compile(r"Bat(wo)?man")
mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group())
mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group())

# The (wo)? part of the regex means that the pattern "wo" is an optional group. The regex will match
# text that has zero instances or one instance of "wo" in it. This is why the regex matches both "Batwoman" and "Batman".
# Using the earlier phone number example, you can make the regex look for phone numbers that do or do not have an area code.
# Enter the following into the interactive shell:

phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
mo1 = phoneRegex.search("My number is 415-555-4242")
print(mo1.group())

mo2 = phoneRegex.search("My number is 555-4242")
print(mo2.group())

# You can think of the ? as saying, "Match zero or one of the group preceding this question mark."

# If you need to match an actual question mark character, escape it with \?


# MATCHING ZERO OR MORE WITH THE STAR:


# The * (called the star) means "match zero or more". The group the precedes the star
# can occur any number of times in the text. It can be absent or repeat over and over again.

batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group())

mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group())

mo3 = batRegex.search("The Adventures of Batwowowowoman")
print(mo3.group())

# For "Batman", the (wo)* part of the regex matches zero instances of wo in the string; for "Batwoman",
# the (wo)* mathces one instance; and for "Batwowowowoman", (wo)* matches 4 times.
# Use an escape character if you need the actual star, e.g. \*


# MATCHING ONE OR MORE WITH THE PLUS


# While * means "match zero or more," the + (or plus) means "match one or more." Unlike the star,
# which does not require its group to appear in the matched string, the group preceding a plus must appear at
# least one. It is not optional.

batRegex = re.compile(r"Bat(wo)+man")
mo1 = batRegex.search("The Adventures of Batwoman")
print(mo1.group())

mo2 = batRegex.search("The Adventures of Batwowowowoman")
print(mo2.group())

mo3 = batRegex.search("The Adventures of Batman")
print(mo3 == None)

# The regex Bat(wo)+man will not match the string "The Adventures of Batman", because at
# least one wo is require by the plus sign.

# If you need to match an actual plus sign character, prefix the plus sign with a backslash to escape it: \+


# MATCHING SPECIFIC REPETITIONS WITH BRACES


# If you have a repeating group, you can use braces to simplify the expression.
# e.g. (Ha){3} will match "HaHaHa".

# Instead of specifing one number you can use a comman to specify a range.
# e.g. (Ha){3,5} will match "HaHaHa", "HaHaHaHa", HaHaHaHaHa".

# You can leave the first or second number blank in the braces to represent the minimum
# or maximum unbounded.
# e.g. (Ha){3,}, will match 3 or more instances | (Ha){5,} will match 5 or more and so on.

# These expressions are identica:
# (Ha){3}
# (Ha)(Ha)(Ha)

# (Ha){3,5}
# ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

haRegex = re.compile(r"(Ha){3}")
mo1 = haRegex.search("HaHaHa")
print(mo1.group())

mo2 = haRegex.search("Ha")
print(mo2 == None)


# PART 4: GREEDY AND NON-GREEDY MATCHING


# Why does (Ha){3,5} match the maximum value given, i.e. "HaHaHaHaHa" in a string is returned
# over it's shorter versions. "HaHaHa" and "HaHaHaHa" are both acceptable.

# Python's regular expression are greedy by default - in abiguous situations
# they will match the longest string possible.
# The non-greedy (also called lazy) version of the braces, which matches the shortest string
# possible, has the closing brace followed by a question mark.

greedyHaRegex = re.compile(r"(Ha){3,5}")
mo1 = greedyHaRegex.search("HaHaHaHaHa")
print(mo1.group())

nongreedyHaRegex = re.compile(r"(Ha){3,5}?")
mo2 = nongreedyHaRegex.search("HaHaHaHaHa")
print(mo2.group())

# NOTE: the questions mark can have two meanings in regex: declaring a non-greedy match
# or flagging an optinoal group. These meanings are not related


# PART 5: THE FINDALL() METHOD:


# Regex objects have a findall() method. While search() will return a Match object of the first matched text
# in the searched string, the findall() method will return the strings of every match in the searched string.

# To see how search() returns a Match object only on the first instance of mathcing text, see below.

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search("Cell: 415-555-9999 Work: 212-555-0000")
print(mo.group())

# findall() will return a list of strings not a match object that needs a .group() to return the match object.
# - as long as there are no groups in the regular expression.
# Each string in the list is a piece of the searched text that matched the regex.

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
print(phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000"))

# If there are groups in the regex, then findall() will return a list of tuples.
# Each tuple represents a found match, and its items are the matched strings for each group.

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")  # has groups
print(phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000"))

# To summarize what findall() returns remember the following:
# When called on a regex with no grups, the method returns a list of strings
# If there are groups, then it returns a list of tuples of strings
# see the above examples as references.


# PART 6: CHARACTER CLASSES


# In the earlier phone number regex example, I learned that \d could stand for any numeric digit.
# That is \d, is shorthand for the regular expression (0|1|2|3|4|5|6|7|8|9).

# Shorthand character class     |     Represents
# \d                            |    Any numeric value from 0 to 9
# \D                            |    Any character that is not a numeric digit from 0 to 9
# \w                            |    Any letter, numeric digit, or the underscore character (this is what we can a word)
# \W                            |   Any character that is not a letter, numeric digit or the underscore character
# \s                            |    Any space, tab, or newline character (this is what we call a "space"
# \S                            |    Any character that is not a space, tab, or newline

# Character classes are nice for shortening regex. The character class [0-5]
# will match only the numbers 0 to 5; this is much shorter than typing (0|1|2|3|4|5)
# NOTE: while \d matches digits and \w matches digits, letters, and the underscorce, there is no
# shorthand character class that matches only letters (Though you can use the [a-zA-Z] character class

xmasRegex = re.compile(r"\d+\s\w+")
print(xmasRegex.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hends, 2 doves, 1 partridge"))

# The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+) followed by a whitespace character (\s),
# followed by one or more letter\digit\underscore characters (\w+). findall() returns all the matching strings of the regex in a list.


# PART 7: MAKING YOUR OWN CHARACTER CLASSES


# Sometimes you want to match a set of characters but the shorthand character classes (\d, \w, \s, etc.) are too broad.
# You can actually make your own character classes using square brackets.
# e.g. [aeiouAEIOU] will match any vowel, both lower and uppercase.

vowelRegex = re.compile(r"[aeiouAEIOU]")
print(vowelRegex.findall("RoboCop eats baby food. BABY FOOD."))

# You can also include ranges of letters or numbers by using a hypen.
# e.g. [a-zA-Z0-9] will match lower and uppercase letters, and numbers

# NOTE: Inside square brackets, the normal regular expression symbols are not interpreted as such.
# I don't need to use an escape character "\" with ., *, ?, or ().

# By placing a caret character (^) just after the character class's opening bracket, you can make a
# negative character class. A negative character class will match all the characters that are not in the character class.

consonantRegex = re.compile(r"[^aeiouAEIOU]")
print(consonantRegex.findall("RoboCop eats baby food. BABY FOOD."))

# now we match every character that isn't a vowel.


# PART 8: THE CARET AND DOLLAR SING characters


# You can use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text.
# Likewise, you can put a dollar sign at the end of a regex to indicate the string must end with this regex pattern.
# You can use both together to indicate that the entire string must match the regex - that is it's not valid to match a substring.
# For example, the r"^Hello" regex matches strings that being with "Hello"

beginsWithHello = re.compile(r"^Hello")
print(beginsWithHello.search("Hello, world!"))
print(beginsWithHello.search("He said hello.") == None)

# The r"\d$" regex matches strings that end with a numeric character from 0 to 9.

endsWithNumber = re.compile(r"\d$")
print(endsWithNumber.search("Your number is 42"))
print(endsWithNumber.search("Your number is forty two.") == None)

# The r"^\d+$" regex string matches strings that both begin AND end with one or more numeric characters.

wholeStringIsNum = re.compile(r"^\d+$")
print(wholeStringIsNum.search("123456789"))
print(wholeStringIsNum.search("12345xyz7890") == None)
print(wholeStringIsNum.search("12 3456789") == None)

# The last two search() calls demonstrate how the entire string must match the regex if ^ and % are used.
# Use the mnemoic "Carrots cost dollars" to remind myself that caret comes first and dollar last.


# PART 9: THE WILDCARD CHARACTER


# The . (or dot) character in a regex is called a wildcard and will match any character
# except for a newline.

atRegex = re.compile(r".at")
print(atRegex.findall("The cat in the hat sat on the flat mat."))

# NOTE: Remember that the dot character will match just one character, which is why the
# match for "flat" is just "lat". To match an actual dot, use an escape character.


# MATCHING EVERYTHING WITH DOT-STAR


# Sometimes you will want to match everything and anything. Say you want to match the string
# "First Name:", followed by any and all text, followed by "Last Name:", and then followed by anything again.
# You can use dot-star (.*) to stand in for that "anything".
# Remeber that the dot character means "any single character except the newline," and the star character means
# "zero or more of the preceding character."

nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = nameRegex.search("First Name: Al Last Name: Sweigart")
print(mo.group(1))
print(mo.group(2))

# The dot-star uses greedy mode: It will always try to match as much text as possible.
# To match any and all text in a non-greedy fashion, use the dot, star, and question mark
# (.*?). Like with braces, the question mark tells Python to match in a non-greedy way.

nongreedyRegex = re.compile(r"<.*?>")
mo = nongreedyRegex.search("<To serve man> for dinner.>")
print(mo.group())

greedyRegex = re.compile(r"<.*>")
mo = greedyRegex.search("<To serve man> for dinner.>")
print(mo.group())

# Both regex roughly translate to "Match an opening angle bracket, followed by anything, followed by a closing angle bracket."
# But the string "<To serve man> for dinner.>" has two possible matches for the closing angle bracket.
# In the non-greedy version of the regex, Python matches the shortest possible string: "<To serve man>". In the greedy version,
# Python matches the longest possible string: "<To serve man> for dinner.>"


# MATCHING NEWLINES WITH THE DOT CHARACTER:


# The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to recompile(), you can make the dot character
# match all characters, including the newline character.

noNewlineRegex = re.compile(".*")
print(noNewlineRegex.search("Serve the public trust.\nProtect the innocent.\nUphold the law.").group())

newlineRegex = re.compile(".*", re.DOTALL)
print(newlineRegex.search("Serve the public trust.\nProtect the innocent.\nUphold the law.").group())

# The regex noNewlineRegex, which did not have re.DOTALL passed to the re.compile() call that created it, will match everything only up to the
# first newline character, whereas newlineRegex, which did have re.DOTALL passed to re.compile(), matches everything. This is why the newlineRegex.search()
# call matches the full string, including its newline characters.


# PART 10: REVEIEW OF REGEX SYMBOLS:


# This chapter covered a lot of notation, so here's a quick review of what you learned about basic regex syntax.

# The ? matches zero or ONE of the preceding group.
# The * matches zero or MORE of the preceding group.
# The + matches one or more of the preceding group.
# The {n} matches exactly n of the preceding group.
# The {n,} matches n or more of the preceding group.
# The {,m} matches 0 to m of the preceding group.
# The {n,m} matches at least n and at most m of the preceding group.
# {n,m}? or *? or +? performs a non-greedy match of the preceding group.
# ^spam means that the string must BEGIN with spam.
# spam$ means that the string must END with spam.
# The . matches any character, except newline characters.
# \d, \w, and \s match a digit, word, or space character, respectively.
# \D, \W, AND \S match anything except a digit, word, or space character respectively.
# [abc] matches any characters between the brackets (such as a, b, c).
# [^abc] matches any character that isn't between the brackets.


# PART 11: CASE-INSENSITIVE MATCHING:


# Normally, regex match text with the exact casing you specify.

regex1 = re.compile("RoboCop")
regex2 = re.compile("ROBOCOP")
regex3 = re.compile("robOcop")
regex4 = re.compile("RobocOp")

# But sometimes you care only about matching the letters without worrying wheter they're uppercase or lowercase.
# To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile().

robocop = re.compile(r"robocop", re.I)
print(robocop.search("RoboCop is part man, part machine, all cop").group())
print(robocop.search("ROBOCOP protects the innocent.").group())
print(robocop.search("Al, why does your programming book talk about robocop so much?").group())


# PART 12: SUBSTITUTING STRINGS WITH THE SUB() METHOD:


# Regex can also substitute new text in place of patterns. sub() is passed two arguments. First, a string to replace a match.
# Second, the string for the regular expression.

namesRegex = re.compile(r"Agent \w+")
print(namesRegex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob."))

# Sometimes you need to use the matched text itself as part of the substitution. In the first argument
# to sub(), you can type \1,\2,\3, and so on. "Enter the text of group 1, 2, 3, and so on, in the subsitution.

# For example, say you want to censor the names of secret agents by showing just the first letters of their names. To do this, you could use the
# regex Agent(\w)\w* and pass r"\1****" as the first argument to sub(). The \1 in that string will be replaced by whatever text was matched by group 1
# -- that is, the (\w) group of the regex.

agentNamesRegex = re.compile(r"Agent (\w)\w*")
print(agentNamesRegex.sub(
    r"\1****", "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent."))


# PART 13: MANAGING COMPLEX REGEXES


# Regex are find if the text pattern you need to match is simple. But matching complicated text patterns might require long,
# convoluted regex. You can mititgate this by telling the re.compile() function to ignore whitespace and comments inside the regex string.
# This "verbose mode" can be enabled by passing the variable re.VERBOSE as the second argument to re.compile()
# Instead of a hard-to-read regular expression like this:

phoneRegex = re.compile(
    r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# You can spread the regex over multiple lines with comments.

phoneRegex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )""", re.VERBOSE)

# NOTE: The previous example uses the triple-quote syntax (""") to create a multiline string so that you can spread the regex definition
# over many lines, making it much more legible.

# The comment rules inside the regex string are the same as Python code.


# PART 14: COMBINING RE.IGNORECASE, RE.DOTALL, AND RE.VERBOSE


# What if you want to use re.VERBOSE to write comments in your regex but also re.IGNORECASE to ignore capitalization?
# Unfortunately, the re.compile() function takes only a single value as its second argument. You can get around this limitation by
# combining the re.IGNORECASE, re.DOTALL, and re.VERBOSE variables using the pipe character (|), which in this context is known as the bitwise or operator

# So if you want a regex that's case-insensitive AND includes newlines to match the dot character, you would form your re.compile() call like this:

someRegexValue = re.compile("foo", re.IGNORECASE | re.DOTALL)

# Including all three options in the second argument will look like this:

someRegexValue = re.compile("foo", re.IGNORECASE | re.DOTALL | re.VERBOSE)

# This syntax is a little old-fashioned and originates from early version sof Python. The details of bitwise operators are beyond the scope of this book.
# CHECK OUT - https://nostarch.com/automatestuff2/ for more information. You can also pass other options
# for the 2nd argument; they're uncommon, buy you can read more about them in the resources, too.


# PROJECT: PLEASE SEE PROJECT.PY FILE


# SUMMARY:
# While a computer can search for text quickly, it must be told precisely what to look for.
# Regex allows you to specify the pattern of characters you are looking for, rather than the exact text itself. In fact, some word processing
# and spreadsheet applications provide find-and-replace features that allow you to search using regex.

# The re module that comes with Python lets you compile Regex objects. These objects have several methods: search() to find a single match,
# findall() to find all matching instances, and sub() to do a find-and-replace substitution of text.

# You can find out more in the offical Python documentation at https://docs.python.org/3/library/re.html.
# Another useful resource is the tutorial website https://www.regular-expressions.info/.


# PRACTICE QUESTIONS:

# 1. What is the function that creates Regex objects.
# re.compile(r"") inside the brackets & quotes is the string you want to match.

# 2. Why are raw strings often used when creating Regex objects.
# so that we can add escape characters or other syntax that Python would interpret as code to execute.

# 3. What does the search() method return?
# the search method will return a match object.

# 4. How do you get the actual strings that match the pattern from a match object?
# store it the match object in a variable, mo = yourRegex.search("") / or .findall() then use the .group() function on the variable name
# NOTE: you can use group(), group(insert numberical number), or groups()

# 5. In the regex created from r"(\d\d\d)-(\d\d\d-\d\d\d\d)", what does gruop 0 cover? Group 1? Group 2?
# Group 0 = all groups together, Group 1 = (\d\d\d), Group 2 = (\d\d\d\-\d\d\d\d\)

# 6. Parentheses and periods have specific meanings in regex syntax. How would you specify that you want a regex to match actual
# parentheses and period characters?
# You can a backslash before each parenthese or period.

# 7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?
#

# 8. What does the | character signify in regular expressions?
# it means "and". When writing rules you can use a | b | c to denote multiple symbols are acceptable.

# 9. What two things does ? character signify in regex?
# first one i forgot, second one is that a match must be made at the first last place of the string.

# 10. What is the difference between the + and * characters in regex?
# + means at least one. * means zero or more

# 11. What is the difference between the {3} and {3,5} characters in regex?
# don't remember

# 12. What do the \d, \w, and \s shortand character classes signify in regex?
# don't remember

# 13. What do the \D, \W, and \S shorthand character classes signify in regex?
# don't remember

# 14. What is the difference between .* and .*??

# 15. What is the character class syntax to match all numbers and lowercase letters?
# [a-zA-Z0-9]

# 16. How do yo umake a regex case-insensitive
# re.I or re.IGNORECASE

# 17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?
# don't remember

# 18. If numRegex = re.compile(r"\d+"), what will numRegex.sub("X", "12 drummers, 11 pipers, five rings, 3 hens" return?
# xx drummers, xx pipers, five rings, x hens

# 19. What does passing re.Verbose as the second argument to re.compile() allow you to do?
