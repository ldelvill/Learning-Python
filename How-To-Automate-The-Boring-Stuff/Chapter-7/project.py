# PROJECT: PHONE NUMBER AND EMAIL ADDRESS EXTRACTOR:

# Say you have to find every phone number and email address in a long web page or document.
# Manually scrolling could take a while. If you have a program that could search the text in your clipboard for phone numbers and email addresses,
# you could simply press ctrl-A to select all text, then ctrl-C to copy it to the clipboard, and run your program.

# NOTE: When tackling a new project, it can be tempting to dive right into writing code. More often than not, it's best to take a step back
# and consider the bigger picture. I recommend first drawing up a high-level plan for what your program needs to do. Don't think about the actual code yet.
# You can worry about that later. Right now, stick to broad strokes.

# 1. Get the text off the clipboard.
# 2. Find all phone numbers and email addresses in the text.
# 3. Paste them onto the clipboard.

# Now, you can start thinking abou how this might work in code. The code will need to do the following:

# 1. Use the pyperclip module to copy and paste strings.
# 2. Create two regexes, one for matching phone numbers and the other for matching email addresses.
# 3. Find all matches, not just the first match, of both regex.
# 4. Neatly format the matched strings into a single string to paste.
# 5. Display some kind of message if no matches were found in the text.

# This list is like a road map for the project. As you write the code, you can focus on each of these steps separately. Each step is fairly manageable and
# expressed in terms of things you already know how to do in Python.


# STEP 1: CREATE A REGEX FOR PHONE NUMBERS:

# First, you have to create a regex to search for phone numbers. Create a new file, enter the following, and save it as phoneAndEmail.py

# The TODO comments are just a skeleton for the program. They'll be replaced as you write the actual code.
# The phone number begins with an optional area code, so the area code group is followed with a question mark.

# Since the area code can be just 3 digits (that is, \d{3}) or three digits within parenthese (that is, \(\d{3}\)), you should have a pipe
# joining those parts. You can add the regex comment # Area code to this part of the multiline string to help you remeber
# what (\d{3}|\(\d{3}\))? is supposed to match.

# The phone number separator can be a space (\s), hyphen (-), or period (.). So these parts should also be joined by pipes.
# The next few parts of the regex are straightforward: three digits, followed by another separator, followed by 4 digits.
# The last part is an optinoal extension made up of any number of spaces followed by ext, x, or ext, followed by two to five digits.

# NOTE: It's easy to get mixed up with regex that contain groups with parenthese () and esccaped paraenthese \(\). Always double check that you're using
# the corect one if you get a "missing ), untermindated subpatter" error message.


# STEP 2: CREATE A REGEX FOR EMAIL ADRESSES:

# You will also need regex that can match email addresses.
# The username part of the email address is one or more characters that can be any of the following:
# lower or uppercase letters, numbers, a dot, an underscore, a percent sign, a plus sign, or a hypen. You can
# make your own class for this.

# The domain and username are separated by an @ symbol. The domain name has a slightly less permissive character class with
# only letters, numbers, periods, and hyphens. And last will be the "dot-com" part (technically known as the top-level domain),
# which can really be dot-anything. This is between two and four characters.

# The format for email addresses has a lot of weird rules. This regex won't match every possible valid email address, but it'll match
# almost any typical email address you'll encounter.


# STEP 3: FIND ALL MATCHES IN THE CLIPBOARD TEXT

# Now that you have specified the regex for phone numbers and email addresses, you can let Python's re module
# do the hard work of finding all the matches on the clipboard. The pyperclip.paste() function will get a string value of the text on
# the clipboard, and findall() regex method will return a list of tuples.

# There is one tuple for each match, and each tuple contains strings for each group in the regex. Remember that group 0 matches the entire regex,
# so the group at index 0 of the tuple is the one you are interested in.

# As you can see at 1, you'll store the matches in a list variable names matches. It starts off as an empty list, and a couple "for" loops. For the email addresses,
# you append group 0 of each match. For the matched phone numbers, you don't want to just append group0. While the program detects phone numbers in several formats,
# you want the phone number appednded to be in a single, standard format. The phoneNum variable contains a string built from groups 1, 3, 5, and 8 of the matched text
# (These groups are the area code, first 3 digits, last four digits, and extension).


# STEP 4: Join the matches into a String for the Clipboard

# Now that you have the email addresses and phone numbers as a list of strings in matches, you want to put them on the clipboard.
# The pyperclip.copy() function takes only a single string value, not a list of strings, so you call the join() method on matches.

# To make it easier to see that the program is working, let's print any matches you find to the terminal. If no phone numbers or email addresses
# were found, the program should tell the user this.


# RUNNING THE PROGRAM:

# For an example open your web broswer to the No starch press contact page at https://nostarch.com/contactus/, press ctrl-a
# to select all the text on the page, and press ctrl-c to copy it to the clipboard. When you run this program, the output wil look
# something like this:

# Copied to clipboard:
# 800-420-7240
# 415-863-9900
# 415-863-9950
# info@nostarch.com
# media@nostarch.com
# academic@nostarch.com
# info@nostarch.com
