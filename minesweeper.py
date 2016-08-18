import sys
import random
# set f to True
f = True


# restarts the program
def restart():
    ...


# map stuffs


def show_grid(grid):
    '''(grid) -> str
    '''
    return '\n'.join(map(show_row, grid))


# map stuffs
def show_row(row):
    '''(cell) -> str
    '''
    return '|'.join(map(show_cell, row))


# map stuffs
def show_cell(cell):
    '''(cell) -> str
    '''
    if cell is None:
        return ' '
    elif cell == '*':
        return 'X'
    else:
        return str(cell)

# ADD MINES TO EMPTY MINE FIELD
while len(mine_locations) < mines:
    row = R(0, 9)
    col = R(0, 9)
    mine_locations.add((row, col))
    background[row][col] = 'M'

for row in range(len(visible_grid)):
    for col in range(len(visible_grid[row])):
        if visible_grid[row][col] == "M":
            continue
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if row + i < 0 or row + i >= len(
                        visible_grid) or col + j < 0 or col + j >= len(
                            visible_grid[row]):
                    break
                elif visible_grid[row + i][col + j] == "M":
                    count += 1

        background[row][col] = count


# checks to see that input matches parameters
def is_valid(guess):
    """ variable -> bool
    If guess is valid, return True; else return False.
    """
    numlist = [1, 2, 3, 4, 5, 6, 7, 8]
    g = guess.split(',')
    # makes sure the list isn't less or greater than 3 units long
    if (len(guess) > 3) or (len(guess) < 3):
        return False
    return (int(g[0]) in numlist) and (int(g[1]) in numlist)


# check for a mine
def is_mine(z):

    # if it's a mine
    if z == '*':

        # print grid and game over
        print('\n' * 30)
        print(show_grid(graygrid))
        while True:
            choose = input('Game Over. Type '
                           '"R" to restart, "Q" to quit: ').strip().lower()

            # options
            if choose == 'q':
                f = False
                return f
            elif choose == 'r':
                restart()

    # if it isn't a mine:
    else:
        f = True
        return f

# the true grid
minegrid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

# the grid you see at first
graygrid = [[None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]]


mines = 6
mine_locations = set()

while len(mine_locations) < mines:
    row = random.randint(0, 7)
    col = random.randint(0, 7)
    mine_locations.add((row, col))
    minegrid[row][col] = '*'

for row in minegrid:
    print(row)
# loop
while f is True:

    # show grid
    print('\n' * 30)
    print(show_grid(graygrid))

    while True:
        # show instructions
        guess = input(
            """Give X and Y coordinates (x, y). Type 'R' to restart, 'Q' to
quit: """).strip().lower()

        # options
        if guess == "r":
            restart()
        elif guess == "q":
            sys.exit()
        elif is_valid(guess):

            # split input into a list
            guess = guess.split(',')

            # set x and y to be what user has input
            x = (int(guess[0]) - 1)
            y = (int(guess[1]) - 1)
            break

    # check for a mine
    graygrid[y][x] = minegrid[y][x]
    f = is_mine((minegrid[y][x]))
