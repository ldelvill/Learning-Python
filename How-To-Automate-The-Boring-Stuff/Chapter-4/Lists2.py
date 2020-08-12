# I split the chapter into 2 parts because of how long it is.

# PART 1: SEQUENCE DATA TYPES:
# Lists aren't the only data types that represent ordered sequences of values.
# For example strings and lists are actually similiar. A string is a "list" of single
# text characters.
# The Python sequence, data types include lists, strings, range objects returned by
# range(), and tuples. Many of the things that can be done with lists can be done
# with sequence data types, e.g. indexing, slicing, for loops with len(), in and not in
# operators.

import copy
name = "Zophie"
print(name[0])
print(name[-2])
print(name[0:4])
print("Zo" in name)
print('z' in name)
print('p' not in name)
for i in name:
    print("* * * " + i + " * * *")

# PART 2: MUTABLE AND IMMUTABLE DATA TYPES
# Lists and strings are different in an important way.
# A list value is a mutable data type: it can have values added, removed, or changed.
# However, a string is immutable: it cannot be changed. Trying to reassign a single
# character in a string results in a TypeError.

name = "Zophie a cat"
# name[7] this results in the error.

# The proper way to "mutate" a string is to use slicing and concatenation to build a new
# string by copying from parts of the old string.

name = "Zophie a cat"
newName = name[0:7] + "the" + name[8:12]  # NOTE: I can also just store the "newName" in "name
print(newName)

# Although a list value is mutabale, the second line of code does not modify the list.

eggs = [1, 2, 3]
eggs = [4, 5, 6]

# an completely new list is over writing the previous list value.
# if you actually want to modify the original list in eggs you would need to do the follow.

eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs)

# changing a value of a mutable data type, changes the value in place and not the
# variable's value. "Passing References" on pg 100 will explain why this is important.

# PART 3: THE TUPLE DATA TYPE
# The tuple data type is similar to the list data type, except in 2 ways.
# 1) tuples have () instead of [].

eggs = ("hello", 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

# The main way that they differ is that tuples are like strings. They are immutable.

# eggs[1] = 99 this will cause an error

# If you only have one value in your tuple you can indicate that the value type is a tuple
# by including a comma at before the ending bracket.

print(type(("hello",)))
print(type(("hello")))

# NOTE: if you need an ordered sequence of values that never change, use a tuple, or that
# you don't want it changed.
# A second benefit is that instead of using lists, is that since they are immutable Python
# will make your code run faster.

# PART 4: CONVERTING TYPES WITH LIST() AND TUPLE() FUNCTIONS
# It's the same as using str() or int().

print(tuple(["cat", "dog", 5]))
print(list(("cat", "dog", 5)))
print(list("hello"))

# NOTE: Converting a tuple to a list is handy if you need a mutable version of the tuple.

# PART 5: REFERENCES
# Variables store strings and integer values.

spam = 42       # 1
cheese = spam   # 2
spam = 100      # 3
print(spam)     # 4
print(cheese)   # 5

# 1) 42 gets assigned to spam, I am actually creating the 42 value in the computer's memory and storing a reference to it.
# 2) when I assign spam to cheese I am copying the reference. Both spam and cheese refer to 42 in the computers memory.
# 3) When you change the value in spam to 100, you are creating a new value and storing the reference in spam. This doesn't affect the value of cheese.

# integers are immutable values that don't change; changing the spam variable is actually making it refer to a
# completely different value in memory.

# Now lists, don't work this way, because list values can change. That is they are mutable.

spam = [0, 1, 2, 3, 4, 5]
cheese = spam  # The reference is being copied, not the list.
cheese[1] = "Hello!"    # This changes the list value
print(spam)
print(cheese)  # The cheese variable still refers to the same list.

# PART 6: IDENTITY AND THE ID() FUNCTION
# You might be wondering why this "weird" behaviour happens with mutable lists and not immutable values
# like integers and strings. All values in Python have unique IDs that can be
# obtained with the id() function. To better understand this behaviour see below:

print(id("Howdy"))

# When Python runs the above code, it creates the string in the computer's memory. The numeric memory address (reference)
# is where the string is stored is returned by the id() function. Address is picked by based on which memory bytes happen to be free
# on your computer at the time.
# Like all strings, "Howdy" is immutable and cannot be changed. If you "change" the string, you are actually creating a new string
# in a different place in the memory.

bacon = "Hello"
print(id(bacon))

bacon += " world!"  # A new string is made from "Hello" and " world!"
print(id(bacon))  # bacon now refers to a completely different string

# As we have talked before, lists can be modified because they are mutable objects. The append() method
# doesn't create a new list object, it changes the existing list object. This is called "modifying the object in-place".

eggs = ["cat", "dog"]  # This creeates a new list
print(id(eggs))
eggs.append("moose")   # modifies the list in place
print(id(eggs))  # still refers to the same list as before

eggs = ["bat", "rat", "cow"]  # this creates a new list, which has a new reference.
print(id(eggs))

# Python's automatic garbage collector deletes any values not being referred to by any variables to free up memory.
# You don't need to worry about how the garbage collector works, which is a good thing. Manual memory management in
# other programming languages is a common source of bugs.

# PART 7: PASSING REFERENCES
# References are important for how arguments get passed to functions. When a function is called the values of the
# arguments are copied to the parameter variables.
# For lists, this means a copy of the reference is used for the parameter.
# To see the consequences of this, refer to PassingReference.py

# PART 8: THE COPY MODULE'S COPY() AND DEEPCOPY() FUNCTIONS
# Although passing around references is the most useful way to deal with lists and dictionaries,
# if the function modifies the list or dict. you may not want these changes in the original list or dict.
# copy() makes a duplicate of a mutable value like a list or dict. It's a new value with a new reference.

# import copy
spam = ["A", "B", "C", "D"]
id(spam)
cheese = copy.copy(spam)
id(cheese)
cheese[1] = 42
print(spam)
print(cheese)

# if the list you need to copy contains lists, then use the copy.deepcopy() function.
# This will copy the inner lists as well.

# A SHORT PROGRAM: CONWAY'S GAME OF LIFE
