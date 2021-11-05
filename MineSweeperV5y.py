import random
debug = False
MineGrid = [["   ", "1", "2", "3", "4", "5", "6", "7", "8"],
         ["   ", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["1 |", "?", "?", "?", "?", "?", "?", "?", "?"],
         ["2 |", "?", "?", "?", "?", "?", "?", "?", "?"],
         ["3 |", "?", "?", "?", "?", "?", "?", "?", "?"],
         ["4 |", "?", "?", "?", "?", "?", "?", "?", "?"],
         ["5 |", "?", "?", "?", "?", "?", "?", "?", "?"],
         ["6 |", "?", "?", "?", "?", "?", "?", "?", "?"],
         ["7 |", "?", "?", "?", "?", "?", "?", "?", "?"],
         ["8 |", "?", "?", "?", "?", "?", "?", "?", "?"]]

Mines = [["?", "?", "?", "?", "?", "?", "?", "?"],
         ["?", "?", "?", "?", "?", "?", "?", "?"],
         ["?", "?", "?", "?", "?", "?", "?", "?"],
         ["?", "?", "?", "?", "?", "?", "?", "?"],
         ["?", "?", "?", "?", "?", "?", "?", "?"],
         ["?", "?", "?", "?", "?", "?", "?", "?"],
         ["?", "?", "?", "?", "?", "?", "?", "?"],
         ["?", "?", "?", "?", "?", "?", "?", "?"]]
def mineplace():#places the mines at the start of the game
    for i in range(0,12):#starts a for loop that counts to 8
        Check = False#defines check
        while Check == False:#places mines
            NewMine1 = random.randint(0,7)
            NewMine2 = random.randint(0,7)
            if Mines[NewMine1][NewMine2] == "M":#checks if a mine is allready in that location
                continue
            else:
                Mines[NewMine1][NewMine2] = "M"
                Check = True
    if debug == True:
        print(*Mines[0], sep="  ")
        print(*Mines[1], sep="  ")
        print(*Mines[2], sep="  ")
        print(*Mines[3], sep="  ")
        print(*Mines[4], sep="  ")
        print(*Mines[5], sep="  ")
        print(*Mines[6], sep="  ")
        print(*Mines[7], sep="  ")
    printgrid()


def printgrid():#displays grid
    print(*MineGrid[0], sep="  ")
    print(*MineGrid[1], sep="  ")
    print(*MineGrid[2], sep="  ")
    print(*MineGrid[3], sep="  ")
    print(*MineGrid[4], sep="  ")
    print(*MineGrid[5], sep="  ")
    print(*MineGrid[6], sep="  ")
    print(*MineGrid[7], sep="  ")
    print(*MineGrid[8], sep="  ")
    print(*MineGrid[9], sep="  ")
    chosemove()


def chosemove():#chooses move
    print("(1)Clear tile")
    print("(2)Place flag")
    print("(3)Remove flag")
    choice = input("")#gets input
    if choice == "1":#remove tile
        minesweep()
    elif choice == "2":#flag tile
        flag()
    elif choice == "3":#remove flag
        removeflag()
    else:
        print("Invalid input")
        chosemove()


def gameover():#gameover script
    print("Gameover")
    menu()#starts up the game

def minesweep():#asks player for cordinate and checks for mines
    minecount = 0
    G1 = input("Please enter grid row:")
    G2 = input("Please enter grid collum:")
    try:
        G1 = int(G1)
    except:
        print("Invalid input please enter a number.")
        minesweep()
    try:
        G2 = int(G2)
    except:
        print("Invalid input please enter a number.")
        minesweep()
    G11 = G1 + 1
    G22 = G2
    G1 = G1 - 1
    G2 = G2 - 1
    if G1 < 0 or G1 > 7 or G2 < 0 or G2 > 7:
        print("Invalid input please enter a number.")
        minesweep()
    
    if Mines[G1][G2] == "M":#checks if player loses
        gameover()
    else:#checks how many mines are surrounding the player
        if G1 == 7 or G2 == 0:
            minecount = minecount
        elif Mines[G1+1][G2-1] == "M":
            minecount = minecount+1
        if G1 == 7:
            minecount = minecount
        elif Mines[G1+1][G2] == "M":
            minecount = minecount+1
        if G1 == 7 or G2 == 7:
            minecount = minecount
        elif Mines[G1+1][G2+1] == "M":
            minecount = minecount+1
        if G2 == 0:
            minecount = minecount
        elif Mines[G1][G2-1] == "M":
            minecount = minecount+1
        if G2 == 7:
            minecount = minecount
        elif Mines[G1][G2+1] == "M":
            minecount = minecount+1
        if G1 == 0 or G2 == 0:
            minecount = minecount
        elif Mines[G1-1][G2-1] == "M":
            minecount = minecount+1
        if G1 == 0:
            minecount = minecount
        elif Mines[G1-1][G2] == "M":
            minecount = minecount+1
        if G1 == 0 or G2 == 7:
            minecount = minecount
        elif Mines[G1-1][G2+1] == "M":
            minecount = minecount+1
        str(minecount)
        MineGrid[G11][G22] = (minecount)
        printgrid()


def flag():#places flag
    G1 = input("Please enter grid row:")
    G2 = input("Please enter grid collum:")
    try:
        G1 = int(G1)
    except:
        print("Invalid input please enter a number.")
        flag()
    try:
        G2 = int(G2)
    except:
        print("Invalid input please enter a number.")
        flag()
    G1 = G1 + 1
    if G1 < 0 or G1 > 8 or G2 < 0 or G2 > 8:
        print("Invalid input")
        flag()
    MineGrid[G1][G2] = ("X")
    printgrid()


def removeflag():
    G1 = input("Please enter grid row:")
    G2 = input("Please enter grid collum:")
    try:
        G1 = int(G1)
    except:
        print("Invalid input please enter a number.")
        removeflag()
    try:
        G2 = int(G2)
    except:
        print("Invalid input please enter a number.")
        removeflag()
    G1 = G1 + 1
    if G1 < 0 or G1 > 8 or G2 < 0 or G2 > 8:
        print("Invalid input")
        removeflag()
    MineGrid[G1][G2] = ("?")
    printgrid()


def rules():
    print("The numbers on the board represent how many bombs are adjacent to a square. For example, if a square has a 3 on it, then there are 3 bombs next to that square. The bombs could be above, below, right left, or diagonal to the square. Avoid all the bombs and expose all the empty spaces to win Minesweeper")
    menu()

def menu():
    global debug
    print("Welcome to mine sweeper")
    print("(1)Play")
    print("(2)Rules")
    menuchoice = input("")
    if menuchoice == "1":
        mineplace()
    elif menuchoice == "2":
        rules()
    elif menuchoice == "debug":
        debug = True
        mineplace()
    else:
        print("invalid menu input")
        menu()
menu()#starts up the game
