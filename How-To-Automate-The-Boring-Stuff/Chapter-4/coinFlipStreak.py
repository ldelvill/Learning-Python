# A program that finds out how often a streak of six heads or a streak of
# six tails comes up in a randomly generated list of heads and tails.

# There are two parts:
# PART 1: Generate a list of randomly selects "heads" and "tails values.
# PART 2: Check if there is a streak in it

# NOTE:
# FIRST: create a list of 100 heads or 100 tails
# get a value of 0 or 1 randomly.
# store the value in a list
# SECOND:check if there is a streak of 6 heads or tails
# start check at the 6th item (so 5th index of the list)
# check the previous 6 items
# check if there is a streak of 6 heads or 6 tails.
# if one is heads and one is tails then we don't have streak.
# if there is a streak of 6 add to number of numberOfStreaks
# if there isn't them up the item check to the next one over.

# TODO: look below. code is pretty much done.

import random
numberOfStreaks = 0

list = []
index = []
# add either 0 or 1 to the list 1000 times
for experimentNumber in range(1000):
    list.append(random.randint(0, 1))

# Code that check is there is a streak of 6 heads or tails in a row.
for i in range(len(list)):
    # starting at the 6 item (5th index)
    # check if the preivous 6 items were all 0's or all 1's
    # if they is a streak, add 1 to keep track
    # this will double count if there is a streak of 7.
    if i >= 5:
        if (list[i - 5]) == 0:
            if (list[i - 4]) == 0:
                if list[(i - 3)] == 0:
                    if list[(i - 2)] == 0:
                        if list[(i - 1)] == 0:
                            if list[i] == 0:
                                numberOfStreaks += 1
                                index.append(i)

        elif (list[i - 5]) == 1:
            if (list[i - 4]) == 1:
                if (list[i - 3]) == 1:
                    if (list[i - 2]) == 1:
                        if (list[i - 1]) == 1:
                            if list[i] == 1:
                                numberOfStreaks += 1
                                index.append(i)
# iterate over the index list
for i in range(len(index)):
    # we want to start at the 1st index, not the 0th index otherwise we get an list out of range error
    if i > 0:
        # TODO: check to see if within a paramter of 6 indexes

        # check if there difference between 2 indexes are 1, if so we need to subtract 1 from number of streaks
        if index[i] - index[i - 1] == 1:
            numberOfStreaks -= 1

print(list)
print(index)
print(numberOfStreaks)
print("Chance of streak: %s%%" % (numberOfStreaks / 100))
