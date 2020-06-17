from GameBoard import GameBoard
from Tiles import Tile
from Score import Score
import Graphics
import stddraw
import time
import test
import random

"""
Created by Jason Jiang and Patrica Lively
"""


class Game():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        e=GameBoard(self.x,self.y)
        self.board = e.drawEmojis()
        self.board

    def checkDraw(self,mDrawX1,mDrawY1):
        rowSwitch = self.y
        switcher = 1
        Graphics.tileSelectedClear(mDrawX1,mDrawY1)
        for index in range(self.y):
            for index in range(self.x):

                if self.board[switcher-1][index].emoji == 1:
                    Graphics.drawMoon(index,switcher)
                if self.board[switcher-1][index].emoji == 2:
                    Graphics.drawAvocado(index,switcher)
                if self.board[switcher-1][index].emoji == 3:
                    Graphics.drawFire(index,switcher)
                if self.board[switcher-1][index].emoji == 4:
                    Graphics.drawCoconut(index,switcher)
                if self.board[switcher-1][index].emoji == 5:
                    Graphics.drawJoy(index,switcher)
                if self.board[switcher-1][index].emoji == 6:
                    Graphics.drawHeart(index,switcher)
                if self.board[switcher-1][index].emoji == 0:
                    Graphics.drawEmpty(index,switcher)

            rowSwitch -= 1
            switcher +=1

        Graphics.eraseScore(self.x,self.y)
        Graphics.drawTotalScore(self.x,self.y,Score.score)

    def ranNum(self):
        return random.randint(1,6)

    def Game(self):
        turn = 0
        turnCounter = 15
        turnCondition = True
        key = True
        while turnCondition:
            stddraw.show(0)
            Graphics.drawTurnCounter(turnCounter)
            Graphics.drawWinThing()
            if turn == 0:
                if stddraw.mousePressed():
                    mx = stddraw.mouseX()
                    my = stddraw.mouseY()

                    if mx < 4.69 and my >= 1 and my < 10:
                        Graphics.clickHelp()
                        for i in range(self.x):
                            if mx > i/1.5 and mx < i/1.5 + (2/3):
                                mDrawX1 = i/1.5
                                mEmojiX1 = i + 1

                        for i in range(self.y+1):
                            if my > i and my < i + 1:
                                mDrawY1 = i
                                mEmojiY1 = i + 1/2

                        for i in range(self.y):
                            for j in range(self.x):
                                if self.board[i][j].x == mEmojiX1 and self.board[i][j].y == mEmojiY1:
                                    e1emoji = self.board[i][j].emoji
                                    e1i, e1j = i , j

                        Graphics.tileSelected(mDrawX1,mDrawY1)
                        turn = 1

            if turn == 1:
                if stddraw.mousePressed():
                    mx = stddraw.mouseX()
                    my = stddraw.mouseY()

                    if mx < 4.69 and my >= 1 and my < 10:

                        for i in range(self.x):
                            if mx > i/1.5 and mx < i/1.5 + (2/3):
                                mEmojiX2 = i + 1

                        for i in range(self.y+1):
                            if my > i and my < i + 1:
                                mEmojiY2 = i + 1/2

                        for i in range(self.y):
                            for j in range(self.x):
                                if self.board[i][j].x == mEmojiX2 and self.board[i][j].y == mEmojiY2:
                                    e2emoji = self.board[i][j].emoji
                                    e2i , e2j = i , j
                    

                        #Swapping the emojis
                        """
                        NOTE THAT THE X POSITIONS ETC HAVE STILL NOT BEEN FIXED
                        11/18/2018 12:14 AM
                        Conversion system new: when x == 1, emoji true position is 1/3, x == 2, 1,
                        x == 3, 5/3
                        """

                        if mEmojiX2 == mEmojiX1 + 1 and mEmojiY2 == mEmojiY1 or mEmojiX2 == mEmojiX1 - 1 and mEmojiY2 == mEmojiY1 or mEmojiY2 == mEmojiY1 + 1 and mEmojiX2 == mEmojiX1 or mEmojiY2 == mEmojiY1 - 1 and mEmojiX2 == mEmojiX1:

                            Graphics.clickHelpClear()
                            self.board[e1i][e1j].emoji = e2emoji
                            self.board[e2i][e2j].emoji = e1emoji

                            counter = 0

                            while test.check(self.board)!=0:
                                self.checkDraw(mDrawX1,mDrawY1)

                                #Erase Vertical
                                if test.getD() == 0:
                                    counter=0
                                    marker = self.board[test.getY()][test.getX()].emoji
                                    while marker!=0:
                                        if test.getY()+counter != 9:
                                            
                                            if marker == self.board[test.getY()+counter][test.getX()].emoji:
                                                self.board[test.getY()+counter][test.getX()].emoji = 0
                                                Score.score += 1 
                                                counter += 1
                                            else:
                                                marker = 0
                                        else:
                                            marker = 0
                                            
                                    self.checkDraw(mDrawX1,mDrawY1)        

                                    #Vertical Drop
                                    count = 0
                                
                                    for j in range(9):
                                        if test.getY()+count+counter<9:
                                            self.board[test.getY()+count][test.getX()].emoji = self.board[test.getY()+count+counter][test.getX()].emoji
                                            self.board[test.getY()+count+counter][test.getX()].emoji = 0
                                
                                            count+=1
                                            
                                    self.checkDraw(mDrawX1,mDrawY1)

                                    temp = 9-counter
                                    
                                    for i in range(counter):
                                        self.board[temp][test.getX()].emoji = self.ranNum()
                                        temp+=1
                                        
                                    self.checkDraw(mDrawX1,mDrawY1)
                                    
                                #Erase Horizontal
                                else:
                                    counter=0
                                    marker = self.board[test.getY()][test.getX()].emoji
                                    while marker!=0:
                                        if test.getX()+counter != 7:
                                            
                                            if marker == self.board[test.getY()][test.getX()+counter].emoji:
                                                self.board[test.getY()][test.getX()+counter].emoji = 0
                                                Score.score += 1 
                                                counter += 1
                                            else:
                                                marker = 0
                                        else:
                                            marker = 0
                                    
                                    self.checkDraw(mDrawX1,mDrawY1)
                                    
                                    #Horizontal Drop
                                    count = 0
                                    for i in range(counter):
                                        count = 0
                                        for j in range(9):
                                            if test.getY()+count<8:
                                                temp = count+1
                                                self.board[test.getY()+count][test.getX()+i].emoji = self.board[test.getY()+temp][test.getX()+i].emoji
                                                self.board[test.getY()+temp][test.getX()+i].emoji = 0
                                                
                                            count+=1
                                    self.checkDraw(mDrawX1,mDrawY1)

                                    for i in range(counter):
                                        self.board[8][test.getX()+i].emoji=self.ranNum()
                                    self.checkDraw(mDrawX1,mDrawY1)
                                    
                                turn = 0

                            #For when it is not a match 3
                            if counter == 0:
                                self.board[e1i][e1j].emoji = e1emoji
                                self.board[e2i][e2j].emoji = e2emoji
                                Graphics.clickHelpClear()
                                Graphics.drawInvalidMatch3()
                                Graphics.clearInvalidSwitch()
                                Graphics.tileSelectedClear(mDrawX1,mDrawY1)
                                turn = 0
                            else:
                                turnCounter -= 1
                        
                        #For when you want to select the tile again
                        elif mEmojiX1 == mEmojiX2 and mEmojiY1 == mEmojiY2:
                            Graphics.clickHelpClear()
                            Graphics.tileSelectedClear(mDrawX1,mDrawY1)
                            turn = 0

                        #For when there is an invaid switch
                        else:
                            Graphics.clickHelpClear()
                            Graphics.tileSelectedClear(mDrawX1,mDrawY1)
                            Graphics.drawInvalidSwitch()
                            Graphics.clearInvalidSwitch()
                            turn = 0

                    else:
                        turn = 1

                #Note, mouse does not need to be pressed in order for this CheckWin
                if turnCounter == 0 and Score.score >= 75:
                    Graphics.drawTurnCounter(turnCounter)
                    turnCondition = False
                    while key:
                        Graphics.drawWinCondition()
                        if stddraw.mousePressed():
                            key = False
                elif turnCounter == 0 and Score.score <= 75:
                    Graphics.drawTurnCounter(turnCounter)
                    turnCondition = False
                    while key:
                        Graphics.drawLossCondition()
                        if stddraw.mousePressed():
                            key = False

                    
Score = Score(0)
game = Game(7,9)
game.Game()