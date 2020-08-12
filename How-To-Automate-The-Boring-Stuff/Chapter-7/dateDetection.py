# Date Detection

import re

# Write a regex that can detect dates in the DD/MM/YYYY format. Assume that the days
# range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999.
# Note that if the day or month is a single digit, it'll have a leading zero.

# Regex doesn't have to detect correct days for each month or for leap years; it will
# accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these string into variables
# named month, day, and year, and write additional code that can detect if it is a valid date.
# April, June, September, and November have 30 days, February has 28 days, and the rest of the months
# have 31 days. February has 29 days in leap years. Leap years are every year evenly divisibly by 4,
# except for eyars evenly divisibly by 100, unless the year is also evenly divisbly by 400.

# Note how this calcuation makes it impossible to make a reasonably sized regex that can detect a valid date.

testOne = "02/04/1998"      # valid date.


testTwo = "00/00/0000"      # lowerbound check for day
testThree = "02/00/0000"    # lowerbound check for month
testFour = "02/04/0000"     # lowerbound check for year

testFive = "32/04/1998"     # upperbound check for day
testSix = "02/13/1998"      # upperbound check for months


testCases = [testOne, testTwo, testThree, testFour, testFive, testSix]


dataRegex = re.compile(r"(\d{2})/(\d{2})/(\d{4})")

for test in testCases:
    print(test)
    mo = dataRegex.search(test)

    day = int(mo.group(1))
    month = int(mo.group(2))
    year = int(mo.group(3))

    if (day > 0) and (day <= 31):
        if (month > 0) and (month <= 12):
            if year > 0:
                # TODO: add 0's infront days or months or years that need them.
                print("%d/%d/%d is a valid date." % (day, month, year))
                continue

    print("%d/%d/%d is not a valid date." % (day, month, year))


# NOTE: the below code doesn't work because the else is attached to the first if statement.
# This means that if the first if statement is True, the else condition will never be met and the program
# will to the next if statement. If that if statement returns False the scope of the first if will be exicted
# and the else will be ignored. You need to review the basics of what an if-else statement does.
# the else block will only execute if the if block is False. Once the if statement is passed True it will execute all code
# in that scope and not execute the else block because that would make no sense. If your if is True. Your else will not
# and should not execute otherwise it defeats the purpose of the if else statement.

# if (day > 0) and (day <= 31):
#    if (month > 0) and (month <= 12):
#        if year > 0:
#            # TODO: add 0's infront days or months or years that need them.
#            print("%d/%d/%d is a valid date." % (day, month, year))
# else:
#    print"%d/%d/%d is not a valid date." % (day, month, year))
