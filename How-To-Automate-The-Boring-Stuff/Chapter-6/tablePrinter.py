# Function that takes a list of lists of strings and displays it in a well-organized
# table with each column right-justified.
# NOTE: WE ARE TO ASSUME THAT EACH LISTS OF STRINGS HAVE AN EQUAL NUMBER OF ITEMS.

# input = list of lists of strings.
# output = table of strings such that each list of strings is printed as a column.
# NOTE: Think of printing same indexed items in each list as a row, i.e. list[0][0], list[1][0], list[2][0], etc.


def printTable(list):
    ''' colWidths stores integers so that we can format r.just(). See line 38. '''
    colWidths = [0] * len(list)

    ''' Finds longest length string in each inner list and stores it in colWidths. '''
    # start with first index of colWidths.
    colWidthsIndex = 0
    # Gives us access to items in the inner list.
    for innerList in list:
        for item in innerList:
            # Update colWidths if needed.
            if len(item) > colWidths[colWidthsIndex]:
                colWidths[colWidthsIndex] = len(item)
        # move to next index of colWidths
        colWidthsIndex += 1

    ''' Prints list items as columns. '''
    # Start by printing items in first row.
    row = 0
    # Main loop: Keeps us printing same indexed items from each list.
    while True:
        # use colWidthsIndex to access formatting of each item in a row, based on what column they belong in. Resets when a row is fully printed.
        colWidthsIndex = 0
        # Gives us access to items in the inner list.
        for innerList in list:
            for item in innerList:
                # Check if we are printing an item that is part of the row.
                if innerList.index(item) == row:
                    print(item.rjust(colWidths[colWidthsIndex]), end=" ")
            # Update colWidthIndex for correct spacing of item in the row.
            colWidthsIndex += 1
        # Update row so that we can print next set of items.
        row += 1
        print("\n")
        # Check if we printed the longest length list, in our list of lists to break loop. NOTE: This is hard coded. It is not correct. NOTE: fixed. condition is based of assumption of inner lists.
        if row <= len(list[0]):
            continue
        else:
            break


tableData = [["apples", "oranges", "cherries", "banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["dogs", "cats", "moose", "goose"]]

printTable(tableData)
