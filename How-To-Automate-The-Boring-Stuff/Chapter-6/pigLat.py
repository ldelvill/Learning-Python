# English to Pig Latin

print("Enter the English message to translate into Pig Latin.")
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []  # A list of the words in Pig Latin.
for word in message.split():
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ""

    # checks if string is empty and if the first index is not part of the alphabet
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        # cuts the string by one character e.g. "4000" goes to "000" and eventually becomes empty.
        word = word[1:]
    # when len(word) is 0 that means we've looped through all characters in the string. It then adds the non-alphabet string to pigLatin lists.
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        # NOTE: this returns control to beginning of loop to avoid a index out of range error that will occur on line 26 when the string is empty.
        continue

    # Separate the non-letters at the end of this word: NOTE: we don't need to check the previous characters as the above already loops through them all. This step is skipped if all characters were looped through already since variable word would eventually be an empty string.
    suffixNonLetters = ""
    # NOTE: when the string is empty you will get an index out of range error. so we use a continue statement on line 21 to avoid this.
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()  # Make the word lowercase for translation

    # Separate the consonants at the start of this word:
    prefixConsonants = ""
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != "":
        word += prefixConsonants + "ay"
    else:
        word += "yay"

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(" ".join(pigLatin))
