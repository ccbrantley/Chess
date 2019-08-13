from turtle import *
import table
import chessPiece

def drawSquareHl():
    color("black", "yellow")
    begin_fill()
    pendown()
    setheading(0)
    forward(74)
    setheading(90)
    forward(74)
    setheading(180)
    forward(74)
    setheading(270)
    forward(74)
    end_fill()
    penup()

def drawBoard():
    setup(width = 800, height = 800, startx=0, starty=0)
    hideturtle()
    speed(0)
    penup()
    tracer(0,0)
    bgpic("./Sprites/board.gif")

    register_shape("./Sprites/pawnWA.gif")
    register_shape("./Sprites/pawnBA.gif")
    
    register_shape("./Sprites/rookWA.gif")
    register_shape("./Sprites/rookBA.gif")

    register_shape("./Sprites/knightWA.gif")
    register_shape("./Sprites/knightBA.gif")

    register_shape("./Sprites/bishopWA.gif")
    register_shape("./Sprites/bishopBA.gif")

    register_shape("./Sprites/kingWA.gif")
    register_shape("./Sprites/kingBA.gif")

    register_shape("./Sprites/queenWA.gif")
    register_shape("./Sprites/queenBA.gif")
    goto(-350,350)

    chessPieces = []
    chessPieces.append(chessPiece.chessPiece('P', 'W', "A2"))
    chessPieces.append(chessPiece.chessPiece('P', 'W', "B2"))
    chessPieces.append(chessPiece.chessPiece('P', 'W', "C2"))
    chessPieces.append(chessPiece.chessPiece('P', 'W', "D2"))
    chessPieces.append(chessPiece.chessPiece('P', 'W', "E2"))
    chessPieces.append(chessPiece.chessPiece('P', 'W', "F2"))
    chessPieces.append(chessPiece.chessPiece('P', 'W', "G2"))
    chessPieces.append(chessPiece.chessPiece('P', 'W', "H2"))

    chessPieces.append(chessPiece.chessPiece('R', 'W', "A1"))
    chessPieces.append(chessPiece.chessPiece('R', 'W', "H1"))

    chessPieces.append(chessPiece.chessPiece('N', 'W', "B1"))
    chessPieces.append(chessPiece.chessPiece('N', 'W', "G1"))

    chessPieces.append(chessPiece.chessPiece('B', 'W', "C1"))
    chessPieces.append(chessPiece.chessPiece('B', 'W', "F1"))

    chessPieces.append(chessPiece.chessPiece('Q', 'W', "D1"))

    chessPieces.append(chessPiece.chessPiece('K', 'W', "E1"))

    
    chessPieces.append(chessPiece.chessPiece('P', 'X', "A7"))
    chessPieces.append(chessPiece.chessPiece('P', 'X', "B7"))
    chessPieces.append(chessPiece.chessPiece('P', 'X', "C7"))
    chessPieces.append(chessPiece.chessPiece('P', 'X', "D7"))
    chessPieces.append(chessPiece.chessPiece('P', 'X', "E7"))
    chessPieces.append(chessPiece.chessPiece('P', 'X', "F7"))
    chessPieces.append(chessPiece.chessPiece('P', 'X', "G7"))
    chessPieces.append(chessPiece.chessPiece('P', 'X', "H7"))

    chessPieces.append(chessPiece.chessPiece('R', 'X', "A8"))
    chessPieces.append(chessPiece.chessPiece('R', 'X', "H8"))

    chessPieces.append(chessPiece.chessPiece('N', 'X', "B8"))
    chessPieces.append(chessPiece.chessPiece('N', 'X', "G8"))

    chessPieces.append(chessPiece.chessPiece('B', 'X', "C8"))
    chessPieces.append(chessPiece.chessPiece('B', 'X', "F8"))
    
    chessPieces.append(chessPiece.chessPiece('Q', 'X', "D8"))

    chessPieces.append(chessPiece.chessPiece('K', 'X', "E8"))
    
    update()
    return chessPieces
