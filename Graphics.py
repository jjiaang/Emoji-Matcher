import stddraw
import math
import picture

def drawBoard(x,y):
    stddraw.setCanvasSize(600,750)
    stddraw.setXscale(0,x)
    stddraw.setYscale(0,y+3)
    stddraw.clear(stddraw.WHITE)

    #Draw the vertical lines
    for i in range(x+1):
        stddraw.line(i/1.5,1,i/1.5,y+1)

    #Draw the horizontal lines
    for i in range(y+1):
        stddraw.line(0,i,x/1.5,i)
    
    drawScore(x,y)
    drawLogo(x,y)
    drawTotalScore(x,y,0)

def drawScore(x,y):
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(20)
    stddraw.text(x-6.2,y+2.5,'Score:')

def drawTotalScore(x,y,score):
    stddraw.setFontSize(20)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(20)
    stddraw.text(x-6.2,y+2,str(score))

def eraseScore(x,y):
    stddraw.setFontSize(0.5)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledCircle(x-6.2,y+2,0.25)

def drawLogo(x,y):
    logo = picture.Picture('logo.png')
    stddraw.picture(logo,x-1,y+2)

def tileSelected(x,y):
    stddraw.setPenColor(stddraw.MAGENTA)
    stddraw.rectangle(x+0.03,y+0.02,(1/1.5)-0.05,0.90)

def tileSelectedClear(x,y):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.rectangle(x+0.03,y+0.02,(1/1.5)-0.05,0.90)

def drawFire(i,rowSwitch):
    fire = picture.Picture('fire.png')
    stddraw.picture(fire,i/1.5+(1/3),rowSwitch+0.5)
    stddraw.show(10)

def drawEmpty(i,rowSwitch):
    empty= picture.Picture('empty.png')
    stddraw.picture(empty,i/1.5+(1/3),rowSwitch+0.5)
    stddraw.show(10)

def drawCoconut(i,rowSwitch):
    coconut = picture.Picture('coconut.png')
    stddraw.picture(coconut,i/1.5+(1/3),rowSwitch+0.5)
    stddraw.show(10)

def drawHeart(i,rowSwitch):
    heart = picture.Picture('heart.png')
    stddraw.picture(heart,i/1.5+(1/3),rowSwitch+0.5)
    stddraw.show(10)

def drawAvocado(i,rowSwitch):
    avocado = picture.Picture('avocado.png')
    stddraw.picture(avocado,i/1.5+(1/3),rowSwitch+0.5)
    stddraw.show(10)

def drawMoon(i,rowSwitch):
    moon = picture.Picture('moon.png')
    stddraw.picture(moon,i/1.5+(1/3),rowSwitch+0.5)
    stddraw.show(10)

def drawJoy(i,rowSwitch):
    joy = picture.Picture('joy.png')
    stddraw.picture(joy,i/1.5+(1/3),rowSwitch+0.5)
    stddraw.show(10)

def drawInvalidSwitch():
    stddraw.setFontSize(20)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(5.5,8,'That is')
    stddraw.text(5.5,7.5,'             an invalid swap!')
    stddraw.show(1500)

def drawInvalidMatch3():
    stddraw.setFontSize(20)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(5.75,8,'You have to swap')
    stddraw.text(5.75,7.5,'      to match a 3!')
    stddraw.show(1500)

def clearInvalidSwitch():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(4.80,7,3.5,2)

def drawTurnCounter(turnCounter):
    fillTurn()
    stddraw.setFontSize(20)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(5.5,5.5,'Turns left:' + str(turnCounter))

def fillTurn():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(4.75,4.7,2.5,1)

def drawWinThing():
    fillWinThing()
    stddraw.setFontSize(20)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(5.65,4.5,'Score above 75')
    stddraw.text(5.55,4,'points to win!')

def fillWinThing():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(4.7,3.75,2,1)

def drawWinCondition():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0.03,4,4.65,2.97)
    stddraw.setFontSize(50)
    stddraw.setPenColor(stddraw.MAGENTA)
    stddraw.text(2.25,5.75,'YOU WIN!')
    stddraw.setFontSize(25)
    stddraw.text(2.25,4.75,'Click to exit')
    stddraw.show(0)

def drawLossCondition():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0.03,4,4.65,2.97)
    stddraw.setFontSize(50)
    stddraw.setPenColor(stddraw.RED)
    stddraw.text(2.25,5.75,'YOU LOSE!')
    stddraw.setFontSize(25)
    stddraw.text(2.25,4.75,'Click to exit')
    stddraw.show(0)

def clickHelp():
    clickHelpClear()
    stddraw.setFontSize(20)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(2,0.5,'Made a Wrong click? Reclick the same tile to try again')

def clickHelpClear():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0,0,5,0.8)