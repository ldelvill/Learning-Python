#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()  # returns all text on the clipboard as one big string.

# Separates lines and adds a star.
# each line in the "one big string" is separated between a \n character. This creates a list item at every \n character.
lines = text.split("\n")
for i in range(len(lines)):  # loop through all indexed in the "lines" list
    lines[i] = "* " + lines[i]  # add a star to each string in "lines" list
# pyperclip.copy() takes in a single string not a list. So we need to turn the list into a single string again.
text = "\n".join(lines)

pyperclip.copy(text)

# NOTE: .paste() will contain anything that is in the clipboard and paste it when called || .copy() will COPY TO the clipboard and not hold anything
# text = pyperclip.paste() doesn't call the function but holds the copied value.
# so in order to use text"in the clipboard we need to assign pyperclip.paste() to a variable.
