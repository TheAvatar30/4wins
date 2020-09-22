import os #os.system('cls')

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
    #test()
    while True:
        string = input("\nInput a number (0-7): ")
        try:
            num = int(string)
            if (0 <= num and num <= 7):
                print("yes")
            else:
                print("out of bounce")
        except ValueError:
            print(f"'{string}' isn't a number")


def test():
    setchar(4, 7, 'x')
    setchar(4, 6, 'x')
    setchar(4, 5, 'x')
    setchar(4, 4, 'x')
    setchar(4, 3, 'x')
    setchar(4, 2, 'x')
    setchar(4, 1, 'x')
    #setchar(4, 0, 'x')
    print(checkmove(4))


def makemove(num: int, player: int):
    for i in range(rows):
        if(getchar(num, i) == ' '):
            if(player == 1):
                setchar(num, i, 'A')
            elif(player == 2):
                setchar(num, i, 'B')


def checkmove(num: int):
    if (getchar(num, 0) == ' '):
        return True
    return False


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
