import random as rnd

rows = 8;
cols = 8;
cross = u'\u253c'
tleft = u'\u251c'
tright = u'\u2524'
tup = u'\u252c'
tdown = u'\u2534'
vline = u'\u2502'
hline = u'\u2500'
ulcorner = u'\u250c'
drcorner = u'\u2518'
urcorner = u'\u2510'
dlcorner = u'\u2514'

start = ' '
board = [[start for i in range(rows)] for j in range(cols)]


def main():
    setchar(5, 1, 'x')
    printboard();
    print(getchar(5, 1))
    # print(cross, tleft, tright, tup, tdown, hline, vline, urcorner,ulcorner,dlcorner,drcorner)


def setchar(x, y, content):
    board[y][x] = content


def getchar(x, y):
    return board[y][x]


def printboard():
    print("")
    print("   ", end='')
    for j in range(cols):
        print(j, end='     ')

    print(f"\n{ulcorner}", end='')
    for j in range(cols):
        if (j < cols - 1):
            print(hline + hline + hline + hline + hline + tup, end='')
        else:
            print(hline + hline + hline + hline + hline + urcorner)

    for i in range(rows):
        print(f"{vline}  ", end='')
        for j in range(cols):
            if (j < cols - 1):
                print(getchar(j, i), end=f'  {vline}  ')
            else:
                print(getchar(j, i) + f"  {vline}")
        if (i < rows - 1):
            print(tleft, end='')
            for j in range(cols):
                if (j < cols - 1):
                    print(hline + hline + hline + hline + hline + cross, end='')
                else:
                    print(hline + hline + hline + hline + hline + tright)
        else:
            print(f"{dlcorner}", end='')
            for j in range(cols):
                if (j < cols - 1):
                    print(hline + hline + hline + hline + hline + tdown, end='')
                else:
                    print(hline + hline + hline + hline + hline + drcorner)


if __name__ == '__main__':
    main()
