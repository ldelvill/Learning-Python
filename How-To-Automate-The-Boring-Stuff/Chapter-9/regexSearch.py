# Opens all .txt files in a directory and searches every line for a user-supplied
# regular expression.

from pathlib import Path
import re

# gets the address of the current working directory and creates a regex for use.
# NOTE: regex use / not \. That's why your code wasn't working smh.
p = Path(Path.cwd())
regexObj = re.compile(input(r"Please enter a regex: "))

# loops over all files in the current working directory that ends with .txt
for textFilePathObj in p.glob("*.txt"):

    # opens the file, stores all the sentences in a list, closes the file.
    textFile = open(textFilePathObj)
    fileContents = textFile.readlines()
    textFile.close()

    # iterates through each sentence in the list, searches for and prints a match if found.
    for sentence in fileContents:
        mo = regexObj.search(sentence)
        if mo != None:
            print("Regex found: " + mo.group())
