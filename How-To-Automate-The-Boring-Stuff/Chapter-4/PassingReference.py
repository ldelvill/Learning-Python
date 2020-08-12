def eggs(someParameter):
    print(id(someParameter))  # used to see if same reference number is being used.
    someParameter.append("Hello")


spam = [1, 2, 3]
print(id(spam))  # used to check reference number.
eggs(spam)
print(spam)

# When eggs() is called, a return value is not used to assign a new value to spam.
# Instead it modifies the list in place, directly.
# spam and someParameter contain the same references because that is what is actually being passed, so both refer to the same
# list.
# NOTE: keep this behavior in mind: forgetting that Python handles list and dicitonary variables
# this way can lead to confusing bugs.
