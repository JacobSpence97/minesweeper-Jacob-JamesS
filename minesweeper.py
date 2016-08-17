def restart():
    ...


def is_mine(z):
    if z == '*':
        input("Game Over. Type 'R' to restart, 'Q' to quit:")
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
         quit:""").strip().lower().split(',')
    if guess == "r":
        restart()
    elif guess == "q":
        break

    graygrid[guess[1]][guess[0]] = minegrid[guess[1]][guess[0]]
    is_mine((minegrid[guess[1]][guess[0]]))
