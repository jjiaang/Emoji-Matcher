import random
from Tiles import Tile
from Grid import Coord

XY=Coord(0,0,0)

def checkRight(grid):
    for i in range(9):
        for j in range(5):
            if grid[i][j].emoji == grid[i][j+1].emoji:
                if grid[i][j+1].emoji==grid[i][j+2].emoji:
                    XY.x = j
                    XY.y = i
                    XY.d = 1
                    return grid[i][j]            
    return 0

def checkDown(grid):
    for i in range(7):
        for j in range(7):
            if grid[i][j].emoji == grid[i+1][j].emoji:
                if grid[i+1][j].emoji==grid[i+2][j].emoji:
                    XY.x = j
                    XY.y = i
                    XY.d = 0
                    return grid[i][j]
    return 0


def check(grid):
    
    if checkDown(grid)!=0:
        return checkDown(grid)
    
    if checkRight(grid)!=0:
        return checkRight(grid)
    
    return 0

def getX():
    return XY.x

def getY():
    return XY.y
    
def getD():
    return XY.d
