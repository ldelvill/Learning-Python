#! python3
# mclip.py - A multi-clipboard program.

import sys
import pyperclip

# STEP 1:
TEXT = {"agree": """Yes, I agree, That sounds fine to me.""",
        "busy": """Sorry, can we do this later this week or next week?""",
        "upsell": """Would you consider making this a monthly donation?"""}

# STEP 2:
if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

# STEP 3:
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for " + keyphrase + " copied to clipboard.")
else:
    print("There is no text for " + keyphrase)
