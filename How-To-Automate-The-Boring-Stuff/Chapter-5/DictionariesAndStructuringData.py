# Dictinonaries and Structuring Data

# PART 1: THE DICTIONARY DATA TYPE
# A dictionary is a mutable collection of many values. Indexes for dictionaries can
# be different data types, unlike lists. Indexes are called keys. Keys have values called
# the key value pair.

myCat = {"size": "fat", "color": "gray", "disposition": "loud"}

# keys are: size, color, disposition
# values are: fat, gray, loud

spam = {12345: "Luggage Combination", 42: "The Answer"}

# PART 2: DICTIONARIES VS LISTS
# Items in dictionaries are unordered. The first item in a list named spam would be spam[0].
# But there is no first item in a dictionary. Ordering of items matters for determining
# wheter 2 lists are the same, but it doesn't matter for dictionaries.

spam = ["cats", "dogs", "moose"]
bacon = ["dogs", "moose", "cats"]
print(spam == bacon)

eggs = {"name": "Zophie", "species": "cat", "age": "8"}
ham = {"species": "cat", "age": "8", "name": "Zophie"}
print(eggs == ham)  # this should be true

# Dictionaries cannot be sliced like lists, or strings.
# Trying to access a key that doesn't exist will result in an error.

spam = {"name": "Zophie", "age": 7}
# spam["color"]  # results in an error

# NOTE: look at birthdays.py

# PART 3: THE KEYS(), VALUES(), AND ITEMS() METHODS
# These methods return list-like values of the dictionary's keys, values or both: keys(), values(), items().
# The returned values aren't true lists, they cannot be modified and do not have an append() method.
# They can be used in for loops.

# this iterates over key values
spam = {"color": "red", "age": 42}
for v in spam.values():
    print(v)

# this iterates over keys
for k in spam.keys():
    print(k)

# this iterates over both. NOTE: Returns values as tuples.
for i in spam.items():
    print(i)

# if you want a tru list from one of the methods, pass the list-like return value to the list() function.

spam = {"color": "red", "age": 42}
print(spam.keys())
print(list(spam.keys()))

# You can also use the multiple assignment trick in a for loop to assign the key and value to
# seperate variables.

spam = {"color": "red", "age": 42}
for k, v in spam.items():
    print("Key: " + k + ", Value: " + str(v))

# PART 4: CHECKING WHETER A KEY OR VALUE EXISTS IN A DICTIONARY
# You can use the "in" and "not in" operators to see if a key exists in a dictioary.

spam = {"name": "Zophie", "age": 7}
print("name" in spam.keys())
print("Zophie" in spam.values())
print("color" in spam.keys())
print("color" not in spam.keys())
print("color" in spam)  # NOTE: this is the short version of "color" in spam.keys()

# PART 5: THE GET METHOD
# It's tedious to check if a key exists before accessing that key's value.
# The get() method takes 2 arguments, the key of the value to retrieve and a fallback value
# to return if that key does not exist.

picnicItems = {"apples": 5, "cups": 2}
print("I am bringing " + str(picnicItems.get("cups", 0)) + " cups.")
print("I am bringing " + str(picnicItems.get("eggs", 0)) + " eggs.")

# There is no key name egg, so we default to 0.

# PART 6: THE SETDEFAULT() METHOD
# You'll often have to set a value in a dictionary for a certain key only if that key does not already have a value.

spam = {"name": "Pooka", "age": 5}
if "color" not in spam:
    spam["color"] = "black"

# the setdefault() method does this. The first argument passed to the method is the key to check for,
# the second argument is the value to set at that key if the key does not exist. If the key does exist,
# the setdefault() method returns the key's value.

spam = {"name": "Pooka", "age": 5}
print(spam.setdefault("color", "black"))
print(spam)
print(spam.setdefault("color", "white"))
print(spam)

# NOTE: refer to characterCount.py . This counts the number of occurrences of each letter in a string.

# PART 7: PRETTY PRINTING
# importing the pprint module gives me access to the pprint() and pformat() functions. This is helpful when
# I need a cleaner display of items in a dictionary than what print() does.

# NOTE: refer to characterCount.py again

# PART 8: USING DATA STRUCTURES TO MODEL REAL-WORLD THINGS
# read section online.

# Tic-Tac-Toe is a good example of using lists and dictionaries as data structures.
# the board is divided into 9 slots named "top-L", "top-M", "top-R", etc., respectively.
# string values represent what is in each slot i.e. 'X', 'O', or " ".

# NOTE: refer to ticTacToe.py

# because I created a data structure to represent a tic tac toe board and wrote code in printBoard() to
# interpret that data structure, I have a program that "models" the tic-tac-toe board.
# I could ahve organized my data struc. differently, but as long as the code works with your data structure,
# I will have a correctly working program.

# PART 8: NESTED DICTIONARIES AND LISTS
# Modeling a tic-tac-toe board was pretty simple. As I model more complicated things, I might need dictionaries
# and list that contain other dictionaries and lists.
# NOTE: remember that lists are useful to contain an ordered series of values, and dictionaries are useful
# for associating keys with values.

# see example below:

allGuests = {"Alice": {"apples": 5, "pretzels": 12},
             "Bob": {"ham sandwiches": 3, "apples": 2},
             "Carol": {"cups": 3, "apple pies": 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print("Number of things being brought:")
print(" - Apples          " + str(totalBrought(allGuests, "apples")))
print(" - Cups           " + str(totalBrought(allGuests, "cups")))
print(" - Cakes          " + str(totalBrought(allGuests, "cakes")))
print(" - Ham Sandwiches " + str(totalBrought(allGuests, "ham sandwiches")))
print(" - Apple Pies     " + str(totalBrought(allGuests, "apple pies")))

spam = {"cat": 1}
