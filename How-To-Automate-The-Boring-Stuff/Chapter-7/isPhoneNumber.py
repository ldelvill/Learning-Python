# checks if there is a phone number in a string


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."

for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
    print("Done")

# for loop notes:
# On each teration of the for loop, a new chunk, substring, of 12 characters from messaage
# is assigend to the variable chunk.
# chunk gets passed into isPhoneNumber to verify if the characters form a phone number
# in our specified format.

# while the string in message is short it could be millions of characters long and the
# program would still run in less than a second.
