def restart():
    ...


def is_mine():
    if "" == '*':
        input("Game Over. Type 'R' to restart, 'Q' to quit:")
    else:
        return True


while True:

    minegrid = [[1, 1, 1, 0], [1, '*', 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]

    graygrid = [[None, None, None, None], [None, None, None, None],
                [None, None, None, None], [None, None, None, None]]

    for row in graygrid:
        print(row)

    guess = input(
        "Give X and Y coordinates (x, y). Type 'R' to restart, 'Q' to quit:")
    if guess == "r":
        restart()
    elif guess == "q":
        break
