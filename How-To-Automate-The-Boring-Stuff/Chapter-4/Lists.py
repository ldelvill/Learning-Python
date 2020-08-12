# LIST:
# Lists and tuples can contain multiple values. Lists can contain other lists
# which can be used to create a hierachical structures.

# PART 1: THE LIST DATA TYPE
# A list is a value that contains multiple values in an ordered sequence.
# List value refers to the list itself, not the values in the list.
# List value: ["cat", "bat", "rat", "elephant"]. aka the list itself or as a whole.
# Values inside the list are called items.

[1, 2, 3]
["cat", "bat", "rat", "elephant"]
["hello", "3.1415", "True", "None", "42"]
spam = ["cat", "bat", "rat", "elephant"]

# The spam variable is assigned the list value. # [] is an empyt lists

# PART 2: GETTING INDIVIDUAL VALUES IN A LIST WITH INDEXES

spam = ["cat", "bat", "rat", "elephant"]
spam[0]
spam[1]
spam[2]
spam[3]
print("Hello, " + spam[0])
print("The " + spam[1] + " ate the " + spam[0] + ".")

# to get an individual value from a list we use an index e.g. spam[0], spam[1], etc.
# The integer inside the square brackets is call the index. The first index is always
# 0.

# Lists can also contain other list values.

spam = [["cat", "bat"], [10, 20, 30, 40, 50]]
spam[0]
print(spam[0][1])
print(spam[1][4])

# The first index dictates which list value to use, the second indicates the value
# within the list.

# PART 3: NEGATIVE INDEXES
# You can also use negative integers for the index. -1 regers to the last index and so on.

spam = ["cat", "bat", "rat", "elephant"]
print(spam[-1])
print(spam[-3])
print("The " + spam[-1] + " is afraid of the " + spam[-3] + ".")

# PART 4: GETTING A LIST FROM ANOTHER LIST WITH SLICES
# A slice can get several values from a list in the form of a new list.

spam[1:4]

# In a slice the first integer is the index where the slice starts. The second integer is the index where the slice ends.
# NOTE: A slice goes up to, but doesn't include the value at the second index.

spam = ["cat", "bat", "rat", "elephant"]
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])

# NOTE: As a shortcut you can leave out one or both of the indexes on either side of the colon in the slice.
# it's the same as using 0 on the left or -1 on the right.

print(spam[:2])
print(spam[1:])
print(spam[:])

# PART 4: GETTING A LIST'S LENGTH WITH THE LEN() FUNCTION
# the len() function will return the number of values that are in a list.

spam = ["cat", "dog", "moose"]
print(len(spam))

# PART 5: CHANGING VALUES IN A LIST WITH INDEXES
# You can use the index of a list to change the value at that index.

spam = ["cat", "bat", "rat", "elephant"]
spam[1] = "aardvark"
print(spam)
spam[2] = spam[1]
print(spam)
spam[-1] = 12345
print(spam)

# PART 6: LIST CONCATENATION AND LIST REPLICATION

print([1, 2, 3] + ["A", "B", "C"])
print(["X", "Y", "Z"] * 3)
spam = [1, 2, 3]
spam = spam + ["A", "B", "C"]
print(spam)

# PART 7: REMOVING VALUES FROM LISTS WITH DEL STATEMENTS
# The del statement will delete values at an index in a list.

spam = ["cat", "bat", "rat", "elephant"]
del spam[2]
print(spam)
del spam[2]
print(spam)

# PART 8: WORKING WITH LISTS
# It's tempting to create many individual variables to store a group of similar values. For example,

catName1 = "Zophie"
catName2 = "Pooka"
catName3 = "Simon"
catName4 = "Lady Macbeth"
catName5 = "Fat-tail"
catName6 = "Miss Cleo"

# This is a bad way to write code.
# refer to AllMyCats1.py
# instead of using repeated variables, we can use a single variable that contains a list.
# reger to AllMyCats2.py

# PART 9: USING FOR LOOPS WITH Lists
# RECAP: We learned about using for loops to execute a block of code a certain
# number of times.

for i in range(4):
    print(i)

# for loop used in a lists:
for i in [0, 1, 2, 3]:
    print(i)

# NOTE: a common technique is to use range(len(someList)) with a for loop QUESTION.
# to iterate over the indexes of a list.

supplies = ["pens", "staplers", "flamethrowers", "binders"]
for i in range(len(supplies)):
    print("Index " + str(i) + " in supplies is: " + supplies[i])

# PART 10: THE IN AND NOT IN OPERATORS
# Use the in or not in operators to see if a value is in or not in a list.
# Evaluates to a boolean value.

print("Howdy" in ["hello", "hi", "howdy", "heyas"])
spam = ["hello", "hi", "howdy", "heyas"]
print("cat" in spam)
print("howdy" not in spam)
print("cat" not in spam)

# refer to MyPets.py

# NOTE: PART 11: QUESTION
# The multiple assignment trick (technically called the tuple unpacking) is a shortcut
# that lets you assign multiple variables with the values in a list in one line of code.

cat = ["fat", "gray", "loud"]
size = cat[0]
color = cat[1]
disposition = cat[2]

# I can use this instead:

cat = ["fat", "gray", "loud"]
size, color, disposition = cat

# The number of variables and the length of th list must be exactly equal otherwise
# I will get an error.

# PART 12: USING THE ENUMERATE() FUNCTION WITH LISTS
# Instaed of using range(len(someList)), I ca nuse enumerate(). This returns two values.
# THe index of the item in the list, and the item in the list itself.

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# enumarte is useful if I need both the item's index and the item itself.

# PART 13: USING THE RANDOM.CHOICE() AND RANDOM.SHUFFLE() FUNCTIONS
# WITH LISTS

# The random module has a few functions that accept lists for arguments.
# random.choice() will return a randomly selected item.
# random.shuffle() will reorder items

# PART 14: AUGMENTED ASSIGNMENT OPERATORS
# Instead of using spam  = spam + 1 .Use spam += 1

# Other augmented statements:
# +=, -=, *=, /=, %=

spam = "Hello,"
spam += " world!"
print(spam)

# PART 15: METHOD
# A method is the same as a function, except it is called on a value. A method
# is typically part of an object or just think after a period e.g
# spam.index("hello"). .index() is the method.

# PART 16:
# index() will return the index of an item in the list.

spam = ["hello", "hi", "howdy", "heyas"]
print(spam.index("hello"))

# If there are duplicate values in a list, the first index appearnce will be
# returned.

# PART 16: ADDING VALUES TO A LISTS WITH APPEND() AND INSERT() METHODS
# To add new values, you can use append() and insert().

spam = ["cat", "dog", "bat"]
spam.append("moose")
print(spam)

# append() will add an arguments to the end of the list.

spam = ["cat", "dog", "bat"]
spam.insert(1, "chicken")
print(spam)

# insert() will add a value at any index.

# NOTE: This is called modifying a list in place. Covered in Mutable and Immutable Data Types.

# PART 17: REMOVING VALUES FROM LISTS WITH THE REMOVE() METHOD
# The remove method will remove an item from a list.

spam = ["cat", "bat", "rat", "elephant"]
spam.remove("bat")
print(spam)

# if an item appears multiple times in the list only the first instance will be removed.

# PART 17: SORTING THE VALUES IN A LIST WITH THE SORT() METHOD
# lists with numbers or strings can be sorted with the sort() method.

spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)  # will organize from least to greatest

spam = ["ants", "cats", "dogs", "badgers", "elephants"]
spam.sort()
print(spam)  # will organize alphabetically

spam.sort(reverse=True)  # this will reverse the order
print(spam)

# There are 3 things to note about sort(). 1) it sorts the list in place, no return value
# 2) I can't sort lists with both numbers and strings.
# 3) It uses the ASCIIbetical order. Uppercase comes first, then lowercase.

# if you need to sort values in regular alphabetical order pass str.lower for the key.

spam = ["a", "z", "A", "Z"]
spam.sort(key=str.lower)
spam

# PART 18: REVERSING THE VALUES IN A LIST WITH THE REVERSE() METHOD
# If you need to reverse the order of a list, call the reverse() method.

spam = ["cat", "dog", "moose"]
spam.reverse()
print(spam)

# NOTE: indentation doesn't matter if you are using a list.

spam = ["apples",
        "oranges",
        "bannans",
        "cats"]
print(spam)

# you can also split up instructions across multiple lines using \ line continuation.

print("Four score and seven " +
      "years ago...")
