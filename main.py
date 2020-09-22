import os  # os.system('cls')

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

rows = 8;
cols = 8;
player1 = ""
player2 = ""
p1symbol = ""
p2symbol = ""

board = [[' ' for i in range(rows)] for j in range(cols)]


def main():
    print("emtpy")


def test():
    while True:
        string = input("\nInput a number (0-7): ")
        if (string == "end"):
            break
        try:
            num = int(string)
            if (0 <= num and num <= 7):
                print("yes")
            else:
                print("out of bounce")
        except ValueError:
            print(f"'{string}' isn't a number")

    setchar(4, 7, 'x')
    setchar(4, 6, 'x')
    setchar(4, 5, 'x')
    setchar(4, 4, 'x')
    setchar(4, 3, 'x')
    setchar(4, 2, 'x')
    setchar(4, 1, 'x')
    # setchar(4, 0, 'x')
    print(checkmove(4))


def makemove(num: int, player: int):
    for i in range(rows):
        if (getchar(num, i) == ' '):
            if (player == 1):
                setchar(num, i, 'A')
            elif (player == 2):
                setchar(num, i, 'B')


def checkmove(num: int):
    if (getchar(num, 0) == ' '):
        return True
    return False


def setchar(x, y, content):
    board[y][x] = content


def getchar(x, y):
    return board[y][x]


def getplayerdata():
    global player1, player2, p1symbol, p2symbol
    player1 = input("Please enter player1's name: ")
    while True:
        p1symbol = input(f"{player1}, Please enter the symbol you wanna play with: ")
        if (len(p1symbol) > 1):
            print("Invalid! Has to be one symbol")
        elif (33 <= ord(p1symbol) and ord(p1symbol) <= 126):
            print(f"{player1}, your symbol is {p1symbol}\n")
            break
        else:
            print("Invalid symbol! Has to be ASCII")

    while True:
        player2 = input("Please Enter Player2's Name: ")
        if (player1 == player2):
            print("Invalid! Name already taken")
        else:
            break

    while True:
        p2symbol = input(f"{player2}, Please enter the symbol you wanna play with: ")
        if (len(p2symbol) > 1):
            print("Invalid! Has to be one symbol (char)")
        elif ((33 <= ord(p2symbol) and ord(p2symbol) <= 126) and not (p1symbol == p2symbol)):
            print(f"{player2}, your symbol is {p2symbol}")
            break
        else:
            print("Invalid! Symbol already taken or none ASCII-symbol")


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
