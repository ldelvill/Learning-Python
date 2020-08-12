# I don't know what this program does yet.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# we want to iterate over the the first inner list
# print every character on that list without a newline character
# when we reach the end we go to the next inner list

# using a for loop: EASIER TO DO WITH A FOR LOOP
# get the first inner list
for y in range(len(grid)):
    # iterate over the inner list
    for x in range(len(grid[y])):
        # print off all items with no newline character
        print(grid[y][x], end="")
        # if we are at the last index, do a normal print command to get to a newline
        if x == (len(grid[y]) - 1):
            print(grid[y][x])

# using a while loop:
x = 0

for y in range(len(grid)):
    # x starts at 0 since we need the 0th index. Break once we reach the length of the innerlist - 1 since we count from 0 and not 1.
    while x != (len(grid[y]) - 1):
        print(grid[y][x], end="")
        x += 1
    print(grid[y][x])
    x = 0
