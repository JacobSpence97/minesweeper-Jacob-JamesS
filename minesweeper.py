import sys
# set f to True
f = True


# restarts the program
def restart():
    ...


# check for a mine
def is_mine(z):

    # if it's a mine
    if z == '*':

        # print grid and game over
        print('\n' * 30)
        for row in graygrid:
            print(row)
        choose = input("Game Over. Type 'R' to restart, 'Q' to quit: ").strip(
        ).lower()

        # options
        if choose == 'q':
            f = False
            return f
        elif choose == 'r':
            restart()
        else:
            is_mine(z)

    # if it isn't a mine:
    else:
        f = True
        return f

# the true grid
minegrid = [[1, 1, 1, 0], [1, '*', 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]

# the grid you see at first
graygrid = [[None, None, None, None], [None, None, None, None],
            [None, None, None, None], [None, None, None, None]]

# loop
while f is True:

    # show grid
    print('\n' * 30)
    for row in graygrid:
        print(row)

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
