import os

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

turn = 1;

lastmove = [2]
alreadyundo = False

board = [[' ' for i in range(rows)] for j in range(cols)]


def main():
    getplayerdata()
    #global player1, player2, p1symbol, p2symbol
    #player1, player2, p1symbol, p2symbol = 'X', 'O', 'X', 'O'
    #test()

    while True:
        os.system('cls')
        locals()
        printboard()
        num = requestnumber()

        try:
            if (checkmove(num)):
                makemove(num)

                if (checkwinhv(num)): #  or checkwind(num)):
                    if (turn == 1):
                        printboard()
                        print(f"{player1}, has won")
                    elif (turn == 2):
                        printboard()
                        print(f"{player2}, has won")
                    break

                nextturn()
        except TypeError:
            print("fail", end='')


def test():
    setchar(3, 7, 'X')
    setchar(3, 6, 'X')
    setchar(4, 7, 'X')
    setchar(4, 6, 'X')
    setchar(4, 5, 'X')
    setchar(5, 7, 'O')
    setchar(5, 6, 'X')
    setchar(5, 5, 'X')


def undo():
    global alreadyundo
    if (alreadyundo == False):
        x = lastmove[0]
        y = lastmove[1]
        setchar(x, y, ' ')
        nextturn()
    else:
        print("You can only undo once each turn")


def requestnumber():
    while True:
        global turn
        if (turn == 1):
            string = input(f"{player1}, it is your turn. Enter a move (number from 0 to 7): ")
        elif (turn == 2):
            string = input(f"{player2}, it is your turn. Enter a move (number from 0 to 7): ")

        if (string == "undo"):
            undo()
            break

        if (checkifnum(string)):
            num = int(string)
            if (0 <= num and num <= 7):
                return num
            else:
                print("Invalid! Out of bounce")
        else:
            print(f"'{string}' is not a number from 0 to 7")


def checkwinhv(move: int):
    locals()

    symbol = ''
    if (turn == 1):
        symbol = p1symbol
    elif (turn == 2):
        symbol = p2symbol

    y = 0
    for i in range(rows):
        if (getchar(move, i) != ' '):
            y = i
            break

    count = 0
    for i in range(rows - 3):
        if (getchar(move, i) == symbol and getchar(move, i + 1) == symbol
                and getchar(move, i + 2) == symbol and getchar(move, i + 3) == symbol):
            return True

    for i in range(cols - 3):
        if (getchar(i, y) == symbol and getchar(i + 1, y) == symbol
                and getchar(i + 2, y) == symbol and getchar(i + 3, y) == symbol):
            return True

    return False


def checkwind(move: int):
    locals()
    leftx = 0
    lefty = 0
    rightx = 0
    righty = 0

    symbol = ''
    if (turn == 1):
        symbol = p1symbol
    elif (turn == 2):
        symbol = p2symbol

    y = 0
    for i in range(rows):
        if (getchar(move, i) != ' '):
            y = i
            break

    for i in range(min(rows, cols)):
        if (isinbounds(leftx - 1, lefty + 1)):
            leftx = leftx - 1
            lefty = lefty + 1
        else:
            break

    for i in range(min(rows, cols)):
        if(isinbounds(rightx + 1, lefty + 1)):
            rightx = rightx + 1
            righty = lefty + 1
        else:
            break

    for i in range(min(rows, cols)):
        try:
            if (getchar(leftx, lefty) == symbol and getchar(leftx + 1, lefty - 1) == symbol
                    and getchar(leftx + 2, lefty - 2) == symbol and getchar(leftx + 3, lefty - 3) == symbol):
                return True
        except IndexError:
            fuckoff()

    for i in range(min(rows, cols)):
        try:
            if (getchar(rightx, righty) == symbol and getchar(rightx - 1, righty - 1) == symbol
                    and getchar(rightx - 2, righty - 2) == symbol and getchar(rightx - 3, righty - 3) == symbol):
                return True
        except IndexError:
            fuckoff()

    return False


def checkifnum(string):
    try:
        num = int(string)
        return True
    except ValueError:
        return False


def nextturn():
    global turn
    if (turn == 1):
        turn = 2
    elif (turn == 2):
        turn = 1


def makemove(num: int):
    global turn, lastmove
    for i in range(rows):
        if (getchar(num, i) == p1symbol or getchar(num, i) == p2symbol):
            if (turn == 1):
                setchar(num, i - 1, p1symbol)
                lastmove = [num, i - 1]
            elif (turn == 2):
                setchar(num, i - 1, p2symbol)
                lastmove = [num, i - 1]
            break
        elif (i == rows - 1):
            if (turn == 1):
                setchar(num, i, p1symbol)
                lastmove = [num, i]
            elif (turn == 2):
                setchar(num, i, p2symbol)
                lastmove = [num, i]
            break


def checkmove(num: int):
    if (0 <= num and num <= 7 and getchar(num, 0) == ' '):
        return True
    return False


def setchar(x, y, content):
    board[x][y] = content


def getchar(x, y):
    return board[x][y]


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
            print("Invalid! Symbol already taken or symbol is none ASCII-symbol")


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


def isinbounds(x: int, y: int):
    if (0 <= x and 0 <= y and x <= cols and y <= rows):
        print(x, y, "in")
        return True
    print(x, y, "out")
    return False

    #try:
    #    c = getchar(x, y)
    #    print(x,y, "in")
    #except IndexError:
    #    print(x, y, "out")
    #    fuckoff()


def fuckoff():
    x: bool = True


if __name__ == '__main__':
    main()
