#pylint: disable-all

import tkinter
import random

class Minesweeper():
    def __init__(self,xsize,ysize,amount):

        self.board = [[None for i in range(ysize)] for i in range(xsize)]
        self.exposedBoard = [[None for i in range(ysize)] for i in range(xsize)]
        self.xsize = xsize
        self.ysize = ysize
        self.mineAmount = amount

        self.populateBoard()

    def getXY(self,x,y):
        return self.board[x][y]

    def getMineNumber(self,x,y):
        count = 0

        for i in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]:
            try:
                if self.board[x+i[0]][y+i[1]] == "mine":
                    count += 1
            except:
                pass

        return count

    def populateBoard(self):

        coords = [random.randint(0,self.xsize-1),random.randint(0,self.ysize-1)]

        for i in range(1,self.mineAmount):
            while self.getXY(coords[0],coords[1]) != None:
                coords = [random.randint(0,self.xsize-1),random.randint(0,self.ysize-1)]

            self.board[coords[0]][coords[1]] = "mine"
            print(coords)

        for x in range(self.xsize):
            for y in range(self.ysize):
                if self.board[x][y] != "mine":
                    self.board[x][y] = self.getMineNumber(x,y)


    def getPrivBoard(self):
        return self.board

    def getBoard(self):
        return self.exposedBoard

m = Minesweeper(10,5,10)
print(m.getPrivBoard())