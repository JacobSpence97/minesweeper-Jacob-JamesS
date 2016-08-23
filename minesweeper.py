import sys
from random import randint as R


# checks to see if on board
def in_bounds(r, c, grid):
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])


# looks to see if it is a mine, in order to change others
def check_if_mine(r, c, grid):
    return grid[r][c] == '*'


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


# check for a mine for game over
def is_mine(z, graygrid):

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
                sys.exit()
            elif choose == 'r':
                game()

    # if it isn't a mine:
    else:
        f = True
        return f


def game():

    # set f to True
    f = True
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

    # give mines
    mines = 10
    mine_locations = set()

    # add mines to empty mine field
    while len(mine_locations) < mines:
        row = R(0, 7)
        col = R(0, 7)
        mine_locations.add((row, col))
        minegrid[row][col] = '*'

    for row in range(len(graygrid)):
        for col in range(len(graygrid[row])):
            if minegrid[row][col] == "*":
                continue
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if in_bounds(row + i, col + j, minegrid) and check_if_mine(
                            row + i, col + j, minegrid):
                        count += 1
            minegrid[row][col] = count

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
                game()
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
        f = is_mine((minegrid[y][x]), graygrid)


game()
