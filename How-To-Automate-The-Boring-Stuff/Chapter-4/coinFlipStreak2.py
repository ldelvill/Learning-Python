# A program that finds out how often a streak of six heads or a streak of
# six tails comes up in a randomly generated list of heads and tails.

# There are two parts:
# PART 1: Generate a list of randomly selects "heads" and "tails values.
# PART 2: Check if there is a streak in it

import random
numberOfStreaks = 0

list = []
index = []
# add either 0 or 1 to the list 10000 times
for experimentNumber in range(10000):
    list.append(random.randint(0, 1))
i = 0
# Code that checks if there is a streak of 6 heads or tails in a row.
while i < (len(list) - 1):
    # starting at the 6 item (5th index)
    # check if the preivous 6 items were all 0's or all 1's
    # if there is a streak, add 1 numberOfStreaks
    if i >= 5:
        if (list[i - 5]) == 0:
            if (list[i - 4]) == 0:
                if list[(i - 3)] == 0:
                    if list[(i - 2)] == 0:
                        if list[(i - 1)] == 0:
                            if list[i] == 0:
                                numberOfStreaks += 1
                                index.append(i)

                                # check if we are at the last 6 items. Otherwise we will accidently skip those and not check them for streaks
                                if (i + 6) <= (len(list) - 1):
                                    i += 6

        elif (list[i - 5]) == 1:
            if (list[i - 4]) == 1:
                if (list[i - 3]) == 1:
                    if (list[i - 2]) == 1:
                        if (list[i - 1]) == 1:
                            if list[i] == 1:
                                numberOfStreaks += 1
                                index.append(i)

                                if (i + 6) <= (len(list) - 1):
                                    i += 6

    i += 1

print(list)
print(index)
print(numberOfStreaks)
print("Chance of streak: %s%%" % (numberOfStreaks / 100))
