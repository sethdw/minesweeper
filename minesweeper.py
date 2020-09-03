#pylint: disable-all

import tkinter
import random

class Minesweeper():
    def __init__(self,size1,size2,amount):

        self.xsize = min(size1,size2)
        self.ysize = max(size1,size2)

        self.board = [[None for i in range(self.ysize)] for i in range(self.xsize)]
        self.exposedBoard = [[None for i in range(self.ysize)] for i in range(self.xsize)]
        self.mineAmount = amount

        self.dead = False

        self.populateBoard()

    def getXY(self,x,y):
        return self.board[x][y]

    def validCoords(self,x,y):
        xvalid = x >= 0 and x < self.xsize
        yvalid = y >= 0 and y < self.ysize
        return xvalid and yvalid

    def getMineNumber(self,x,y):
        count = 0

        for i in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]:
            if self.validCoords(x+i[0],y+i[1]):
                if self.getXY(x+i[0],y+i[1]) == "mine":
                    count += 1

        return count

    def populateBoard(self):

        coords = [random.randint(0,self.xsize-1),random.randint(0,self.ysize-1)]

        for i in range(self.mineAmount):
            while self.getXY(coords[0],coords[1]) != None:
                coords = [random.randint(0,self.xsize-1),random.randint(0,self.ysize-1)]

            self.board[coords[0]][coords[1]] = "mine"
            print(coords)

        for x in range(self.xsize):
            for y in range(self.ysize):
                if self.board[x][y] != "mine":
                    self.board[x][y] = self.getMineNumber(x,y)

    def reveal(self,x,y):
        if not self.validCoords(x,y):
            return 

        if self.exposedBoard[x][y] == self.getXY(x,y):
            return

        if self.getXY(x,y) != 0:
            self.exposedBoard[x][y] = self.getXY(x, y)
            return

        for i in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]:
            self.exposedBoard[x][y] = self.board[x][y]
            self.reveal(x+i[0], y+i[1])

    def select(self,x,y):
        if self.dead:
            return 0

        if self.getXY(x,y) == "mine":
            self.dead = True
            self.exposedBoard[x][y] = self.getXY(x,y)
            return 0

        self.reveal(x,y)
        return 1

    def getPrivBoard(self):
        return self.board

    def getBoard(self):
        return self.exposedBoard

    def getBoardFancy(self):
        ret = ""
        for x in range(self.xsize):
            for y in range(self.ysize):
                if self.exposedBoard[x][y] == "mine":
                    ret += "m"
                elif self.exposedBoard[x][y] == None:
                    ret += "?"
                else:
                    ret += str(self.exposedBoard[x][y])

                ret += " "
            ret += "\n"

        return ret

s1 = int(input("size 1: "))
s2 = int(input("size 2: "))
ms = int(input("number of mines: "))

m = Minesweeper(s1,s2,ms)
print(m.getBoardFancy())

while not m.dead:
    x = input("x: ")
    y = input("y: ")
    m.select(int(y),int(x))
    print(m.getBoardFancy())

print("you died")