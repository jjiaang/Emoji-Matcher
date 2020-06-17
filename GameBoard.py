import random
import Graphics
import stddraw
from Tiles import Tile

"""
1.) Generate a board with a bunch of random numbers from 1-6 representing our tiles.
11/8/2018, idea, try implementing a counter1 and a counter2, for rows and columns respectively. If BOTH counters are == 0: Then you have a valid board

Finished as of 2018-11-09

2.) Assign all values from 1-6 to a special picture. In this case we will use emois.
1 = moon.png
2 = avocado.png
3 = fire.png
4 = coconut.png
5 = joy.png
6 = heart.png

2.) Generate pictures of the emojis based on the the numbers coorelating to the images.
Sample would be, a for loop, then to check all the tiles, and if a tile's number and picture index match
then put the picture on it

```
for i in range(y):
        for i in range(x):
            stddraw.picture(apple,i/1.5+(1/3),rowSwitch+0.5)
        rowSwitch +=1
```

"""

class GameBoard():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def setBoard(self):
        notBoard = True

        while notBoard:

            counterRow = 0
            counterCol = 0

            row = 0
            col = 0

            board = [[random.randint(1,6) for i in range(self.x)] for j in range(self.y)]
        
            #row Check to see if duplicate
            for index in range(self.y):    
                for index in range(self.x):
                    if index < self.x - 2:
                        if board[row][index] == board[row][index + 1] and board[row][index] == board[row][index + 2]:
                            counterRow += 1
                row += 1

            #Column checks for duplicates
            for index in range(self.y):
                for index in range(self.x):
                    if col < self.y-2:
                        if board[col][index] == board[col + 1][index] and board[col][index] == board[col + 2][index]:
                            counterCol += 1
                col +=1

            if counterCol == 0 and counterRow == 0:
                notBoard = False
                TileBoard = self.convertBoard(board)
                return TileBoard

    def convertBoard(self, board):

        TileBoard = [[Tile(0,0,0) for x in range(7)] for y in range(9)]

        y = 1.5
        for i in range(9):
            x= 1
            for j in range(7):
                emoji = board[i][j]
                TileBoard[i][j] = Tile(emoji,x,y)
                x += 1          
            y+=1
        return TileBoard

    def drawEmojis(self):
        board = self.setBoard()       
        Graphics.drawBoard(self.x,self.y)
        rowSwitch = self.y
        switcher = 1
        for index in range(self.y):
            for index in range(self.x):

                if board[switcher-1][index].emoji == 1:
                    Graphics.drawMoon(index,switcher)
                if board[switcher-1][index].emoji == 2:
                    Graphics.drawAvocado(index,switcher)
                if board[switcher-1][index].emoji == 3:
                    Graphics.drawFire(index,switcher)
                if board[switcher-1][index].emoji == 4:
                    Graphics.drawCoconut(index,switcher)
                if board[switcher-1][index].emoji == 5:
                    Graphics.drawJoy(index,switcher)
                if board[switcher-1][index].emoji == 6:
                    Graphics.drawHeart(index,switcher)

            rowSwitch -= 1
            switcher +=1

        return board