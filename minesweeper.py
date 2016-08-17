def restart():
    ...


minegrid = [[1, 1, 1, 0], [1, '*', 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]
graygrid = [[None, None, None, None], [None, None, None, None],
            [None, None, None, None], [None, None, None, None]]

for row in graygrid:
    print(row)

guess = input()
if guess == "r":
    restart()
elif guess == "q":
    break
