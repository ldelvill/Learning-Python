# Takes a list, returns a string with all items seperated by commas and a space.
# The word and is inserted before the last item.

# NOTE:
# FIRST STEP: add commas to every item in the list.
# SECOND STEP: add "and" as the second last item in the list.
# THIRD STEP: turn the list into a string
# Needed to make sure every item in the list was a string value first.


def commaCode(list):
    string = ""
    # converts every item to a string
    for i in range(len(list)):
        list[i] = str(list[i])

    # this loops over every item but the last in the list
    for i in range(len(list) - 1):
        # concatenates a comma and a space to items in the list
        list[i] += ", "

    # this inserts "and" before the last index
    list.insert(-1, "and ")

    # adds every item to the string variable
    for i in range(len(list)):
        string += list[i]

    return string


spam = ["apples", "bananas", "tofu", "cats"]
spam = [1, 2, 3, 4]
print(commaCode(spam))
