from turtle import *
import draw
import table
import chessPiece
global gameMap
global gameState
global admin
admin = chessPiece.chessPiece("P", "A", "Z1")
gameMap = table.table()
gameState = True

def userClick(x, y):
    sector = admin.coToSector(x,y)
    goto(x,y)
    if(gameMap.tableMapTest.get(sector) != None):
        onscreenclick(secondClick,1)
        
def secondClick(x,y):
    sector = admin.coToSector(xcor(),ycor())
    if(gameMap.tableMapTest.get(sector) != None):
        playPiece = gameMap.tableMapTest.get(sector)
        if(gameMap.getPlayerTurn() == playPiece.holder):
            scdSector = admin.coToSector(x,y)
            playPiece = gameMap.tableMapTest.get(sector)
            if(playPiece.movPiece(scdSector,gameMap.tableMapTest) == True):
                del gameMap.tableMapTest[sector]
                gameMap.updateTable(scdSector, playPiece)
                if(gameMap.getPlayerTurn() == "W"):
                    gameMap.updatePlayerTurn("X")
                else:
                    gameMap.updatePlayerTurn("W")
    listenUser()
def escProg():
    bye()
    
def listenUser():
    listen()
    onscreenclick(userClick,1)

def startHere(chessPieces):
    for chessPiece in chessPieces:
        gameMap.updateTable(chessPiece.space, chessPiece)
    if(gameState == True):
        listenUser()
