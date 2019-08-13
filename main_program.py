from turtle import *
import draw
import instructions
import table
import chessPiece
gameMap = table.table()
chessPieces = draw.drawBoard()
instructions.startHere(chessPieces)
done()
