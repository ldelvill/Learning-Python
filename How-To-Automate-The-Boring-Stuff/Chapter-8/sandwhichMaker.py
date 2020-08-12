import pyinputplus as pyip

# write a program that asks users for their sandwhich preferences. The program should use
# PyInputPlus to ensure that they enter valid input, such as:

# Using inputMenu() for a bread type: wheat, white, or sourdough
# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu
# Using inputYesNo() to ask if they want cheese
# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
# Using inputInt() to ask how many sandwhiches they want. Make sure this number is 1 or more.

# Come up with prices for each of these options, and have your program display a total cost after
# the user enters their selection.

breadResponse = pyip.inputMenu(["wheat", "white", "sourdough"], numbered=True)

proteinResponse = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], numbered=True)
# this will store the string "yes" or "no"
cheeseResponse = pyip.inputYesNo("Would you like cheese (Please enter 'Yes' or 'No')?\n")

if cheeseResponse == "yes":
    cheeseSelectionResponse = pyip.inputMenu(["cheddar", "swiss", "mozzarella"], numbered=True)

numberOfSandwhiches = pyip.inputInt(
    "How many sandwhichs would you like (Enter a positive whole number)?\n")

if cheeseResponse == "yes":
    print("You have ordered: \nBread: %s \nProtein: %s \nCheese: %s \nNumber of Sandwhiches: %d" % (
        breadResponse, proteinResponse, cheeseSelectionResponse, numberOfSandwhiches))
else:
    print("You have ordered: \nBread: %s \nProtein: %s \nNumber of Sandwhiches: %d" %
          (breadResponse, proteinResponse, numberOfSandwhiches))
