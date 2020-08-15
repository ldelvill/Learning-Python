# Mad Libs program
# Reads in texts files and lets the user add their own text anywhere to the words
# ADJECTIVE, NOUN, ADVERB, OR VERB in the text file.

from pathlib import Path

textFile = open(Path.cwd() / "test.txt")
fileContent = textFile.read()
textFile.close()

wordsToReplace = ["ADJECTIVE", "NOUN", "VERB", "ADVERB"]
wordsToReplacePunc = ["ADJECTIVE.", "NOUN.", "VERB.", "ADVERB."]
punctuation = [".", "?", "!"]
x = fileContent.split()

for i in range(len(x)):

    if x[i] in wordsToReplace:
        word = input("Enter a %s:" % x[i])
        x[i] = word

    if x[i] in wordsToReplacePunc:
        word = input("Enter a %s:" % x[i])
        x[i] = word + "."

y = " ".join(x)
print(y)

newFile = open("new.txt", "w")
newFile.write(y + "\n")
newFile.close()

# NOTE: slicing starts at the first index given (inclusive) and ends at the last index given (exclusive).
# So the last index does not get included.
