# To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your own
# without importing it. This program will prompt the user with 10 multiplication questions, ranging from
# 0 x 0 to 9 x 9. You'll need to implement the following features:

# If the user enters the correct answer, the program displays "Correct!" for 1 second and moves on to the next question.
# The user gets three tries to enter the correct answer before the program moves on to the next question.
# Eight seconds after first displaying the question, the question is maarked as incorrect even if the user
# enters the correct answer after the 8-second limit.

# TODO: After eight seconds the script returns control to the main loop

import random
import time

questionNumber = 1
numberOfTries = 0

while True:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    print("Question %d" % (questionNumber))

    while numberOfTries < 3:
        response = input(((str(num1) + "*" + str(num2) + " =")))

        if int(response) == (num1 * num2):
            print("Correct!")
            time.sleep(1)
            numberofTries = 0
            questionNumber += 1
            break
        else:
            numberOfTries += 1

    if numberOfTries >= 3:
        numberOfTries = 0
        questionNumber += 1
