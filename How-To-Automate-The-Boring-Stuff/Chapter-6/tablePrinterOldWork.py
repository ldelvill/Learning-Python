listIndex = 0
innerListIndex = 0

while innerListIndex < len(list[-1]):
        while listIndex < len(list):
            print(list[listIndex][innerListIndex].rjust(colWidths[colWidthsIndex]), end=" ")
            listIndex += 1
            colWidthsIndex += 1
        innerListIndex += 1
        listIndex = 0
        colWidthsIndex = 0
