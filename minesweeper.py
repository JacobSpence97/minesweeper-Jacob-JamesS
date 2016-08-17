def restart():
    ...


def is_mine(z):
    if z == '*':
        choose = input("Game Over. Type 'R' to restart, 'Q' to quit: ").strip(
        ).lower()
        if choose == 'q':
            return False
        elif choose == 'r':
            restart()
        else:
            return False
    else:
        return True


minegrid = [[1, 1, 1, 0], [1, '*', 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]

graygrid = [[None, None, None, None], [None, None, None, None],
            [None, None, None, None], [None, None, None, None]]
while True:

    print('\n' * 30)
    for row in graygrid:
        print(row)

    guess = input(
        """Give X and Y coordinates (x, y). Type 'R' to restart, 'Q' to
quit: """).strip().lower().split(',')
    if guess == "r":
        restart()
    elif guess == "q":
        break

    x = (int(guess[0]) - 1)
    y = (int(guess[1]) - 1)

    graygrid[y][x] = minegrid[y][x]
    is_mine((minegrid[y][x]))
