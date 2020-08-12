# The replicates a magic 8 ball.
# This produces a random number to use for the index, regardless of the size of the
# list. I'll get a random number between 0 and the value of len(messages) - 1.
# The benefit of this approach is that you can easily add and remove strings to the
# message list without changing other lines of code. If you later update the code
# there will be fewer lines you have to change and fewer chances for you to introduce
# bugs.

import random

messages = ["It is certain",
            "It is decidely so",
            "Yes definitely",
            "Reply hazy try again",
            "Ask again later",
            "Concentrate and ask again",
            "My reply is no",
            "Outlook not so good",
            "Very doubtful"]

print(messages[random.randint(0, len(messages) - 1)])
