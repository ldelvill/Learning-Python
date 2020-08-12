# PROJECT: MULTIPLICATION QUIZ

# PyInputPlus's features can be useful for creating a timed multiplication quiz. By setting the allowRegexes,
# blockRegexes, and limit keyword argument to pyip.inputStr(), you can leave most of the implementation to
# PyInputPlus. The less code you need to write, the faster you can write your programs. Let's create a program
# that poses 10 multiplication problems to the user, where the valid input is the problem's correct answer.
# Open a new file editor tab and save the file as multiplicationQuiz.py


# First, we'll import pyinputplus, random, and time. We'll keep track of how many questions the program asks
# and how many correct answers the user gives with the variables numberOfQuestions and correctAnswers.
# A for loop will repeatedly pose a random multiplication problem 10 times:


# The pyip.inputStr() function will handle most of the features of this quiz program.
# The argument we pass for allowRegexes is a list with the regex string '^%s$',
# where %s is replaced with the correct answer. The ^ and % characters ensure that
# the answer begins and ends with the correct number, though PyInputPlus trims any
# whitespace from the start and end of the user’s response first just in case they
# inadvertently pressed the spacebar before or after their answer.
# The argument we pass for blocklistRegexes is a list with ('.*', 'Incorrect!').
# The first string in the tuple is a regex that matches every possible string.
# Therefore, if the user response doesn’t match the correct answer, the program will
# reject any other answer they provide. In that case, the 'Incorrect!' string is
# displayed and the user is prompted to answer again. Additionally, passing 8 for
# timeout and 3 for limit will ensure that the user only has 8 seconds and 3 tries to
# provide a correct answer:


# If the user answers after the 8-second timeout has expired, even if they answer correctly,
# pyip.inputStr() raises a TimeoutException exception. If the user answers incorrectly more
# than 3 times, it raises a RetryLimitException exception. Both of these exception types are
# in the PyInputPlus module, so pyip. needs to prepend them:


# Remember that, just like how else blocks can follow an if or elif block,
# they can optionally follow the last except block. The code inside the following
# else block will run if no exception was raised in the try block. In our case,
# that means the code runs if the user entered the correct answer:


# No matter which of the three messages, “Out of time!”, “Out of tries!”, or “Correct!”,
# displays, let’s place a 1-second pause at the end of the for loop to give the user time
# to read it. After the program has asked 10 questions and the for loop continues,
# let’s show the user how many correct answers they made:


# PyInputPlus is flexible enough that you can use it in a wide variety of programs that take keyboard
# input from the user, as demonstraded by the programs in this chapter.
