# Updatable Multi-Clipboard

# Save new strings to load to the clipboard without having to modify the source code.

#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# Deletes a keyword from the shelf
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    mcbShelf.pop(sys.argv[2], None)
elif len(sys.argv) == 2 and sys.argv[1].lower() == "delete-all":
    keys = list(mcbShelf.keys())
    for key in keys:
        mcbShelf.pop(key, None)
elif len(sys.argv) == 2:
    # List of keywords and load content.
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()
