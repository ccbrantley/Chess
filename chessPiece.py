from turtle import *
import table
class chessPiece:
    xToKey = {1 :'A', 2 : 'B', 3 : 'C', 4 : 'D',
               5 : 'E', 6 : 'F', 7 : 'G', 8 : 'H'}
    xFrmKey = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4,
               'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8}
    imageNames = {'NW' : "./Sprites/knightWA.gif", 'NX' : "./Sprites/knightBA.gif",
                  'BW' : "./Sprites/bishopWA.gif", 'BX' : "./Sprites/bishopBA.gif",
                  'QW' : "./Sprites/queenWA.gif",  'QX' : "./Sprites/queenBA.gif",
                  'KW' : "./Sprites/kingWA.gif",   'KX' : "./Sprites/kingBA.gif",
                  'PW' : "./Sprites/pawnWA.gif",   'PX' : "./Sprites/pawnBA.gif",
                  'RW' : "./Sprites/rookWA.gif",   'RX' : "./Sprites/rookBA.gif"}
    
    # typeChar -> type of chess piece
    # holder -> team (ownership)
    # stampId -> for removal of chess pieces
    # space -> position on the board, e.g. A1
    def __init__(self, typeChar, holder, space):
        if(space != "Z1"):
            self.firstTurn = True
            self.typeChar = typeChar
            self.holder = holder
            self.space = space
            self.imgAddr = self.imageNames[self.typeChar + self.holder]
            self.stampId = ""
            self.setPlayType()
            self.playType
            self.populateTable(self.space)
        
    def deletePiece(self):
        clearstamp(self.stampId)
        self.stampId = ""
        
    def stampPiece(self, x, y):
        shape(self.imgAddr)
        goto(x, y+30)
        self.stampId = stamp()
        
    def populateTable(self, newSpace):
        xCo, yCo = self.sectorToCo(newSpace)
        self.stampPiece(xCo, yCo)
        self.space = newSpace
        
    def movPiece(self, newSpace, tableMap):
        available = self.availableMoves(tableMap)
        xCo, yCo = self.sectorToCo(newSpace)
        if(available != None):
            if(newSpace in available):
                # Checking if space is populated
                if newSpace in tableMap.keys():
                    tableMap[newSpace].deletePiece()               
                self.deletePiece()
                self.stampPiece(xCo, yCo)
                self.space = newSpace
                self.firstTurn = False
                return True
        else:
            return False     
        
    def freeSpace(self, sector, tableMap):
        chessPiece = tableMap.get(sector)
        if(chessPiece == None):
            return True
        else:
            if(self.typeChar == "P"):
                return False
            if(chessPiece.holder != self.holder):
                return True
            else:
                return False
            
        # {x=0} -> don't update x
    def editSpace(self, x, y):
        sectorSplit = list(self.space)
        numericChar = sectorSplit[1]
        if(0 < x < 9):
            alphaChar = self.xToKey[x]
        else:
            alphaChar = sectorSplit[0]
        return (alphaChar + str(y))
    
    def sectorToInt(self,sector):
        sectorSplit = list(sector)
        xInt = self.xFrmKey[sectorSplit[0]]
        yInt = int(sector[1])
        return xInt, yInt
        
    # finding x and y coordinates for stamp from sector on board    
    def sectorToCo(self, sector):
        sectorSplit = list(sector)
        xCo = ((self.xFrmKey[sectorSplit[0]] -5)*74)+37
        yCo = ((int(sectorSplit[1]) -5)*74)+37
        return (xCo, yCo)
    
    def coToSector(self, xB, yB):
        xPos = (xB//74)+5
        yPos = (yB//74)+5
        if ((0 < xPos < 9) and (0 < yPos < 9)):
            return (self.xToKey[xPos] + str(int(yPos)))
        else:
            return None

    def pawnOt(self,tableMap):
        availableMove = list()
        curSector = list(self.space)
        if(self.typeChar == "P"):
            if(self.holder == "W"):
                yMulti = 1
            else:
                yMulti = -1
            if(int(self.xFrmKey[curSector[0]]) > 1):
                tLSector = self.xToKey[self.xFrmKey[curSector[0]]-1]+ str(yMulti+int(curSector[1]))
                if(tLSector in tableMap.keys()):
                    chessPiece = tableMap.get(tLSector)
                    if(self.holder != chessPiece.holder):
                        availableMove.append(tLSector) 
            if(int(self.xFrmKey[curSector[0]]) < 8):
                tRSector = self.xToKey[self.xFrmKey[curSector[0]]+1]+ str(yMulti+int(curSector[1]))
                if(tRSector in tableMap.keys()):
                    chessPiece = tableMap.get(tRSector)
                    if(self.holder != chessPiece.holder):
                        availableMove.append(tRSector) 
        return availableMove

    #Collision Upwards - > U
    #Collision Downwards -> D
    #Collision Leftwards -> L
    #Collision Rightwards -> R
    #Collision Diagonal -> UL
    #Collision Diagonal -> UR
    #Collision Diagonal -> DL
    #Collision Diagonal -> DR
    #Reports Collision at Sector position, not before
    def collisionDetection(self, colType, tableMap):
        xInt, yInt = self.sectorToInt(self.space)
        if (colType == "U"):
            for y in range(yInt+1,9):
                checkSector = self.editSpace(xInt,y)
                if(checkSector in tableMap):
                    return y+1
            return 9
        if (colType == "D"):
            for y in range(yInt-1,0,-1):
                checkSector = self.editSpace(xInt,y)
                if(checkSector in tableMap):
                    return y-1
            return 0
        if (colType == "L"):
            for x in range(xInt-1,0,-1):
                checkSector = self.editSpace(x,yInt)
                if(checkSector in tableMap):
                    return x-1
            return 0
        if (colType == "R"):
            for x in range(xInt+1,9):
                checkSector = self.editSpace(x,yInt)
                if(checkSector in tableMap):
                    return x+1
            return 9
        if (colType == "UL"):
            x=xInt-1
            for y in range(yInt+1,9):
                checkSector = self.editSpace(x,y)
                if(checkSector in tableMap):
                    return x,y
                else:
                    if((x>1)and(y<8)):
                        x-=1
                    else:
                        return x,y
            return 1,8
        if (colType == "UR"):
            x=xInt+1
            for y in range(yInt+1,9):
                checkSector = self.editSpace(x,y)
                if(checkSector in tableMap):
                    return x,y
                else:
                    if((x<8)and(y<8)):
                        x+=1
                    else:
                        return x,y
            return 8,8
        if (colType == "DL"):
            x=xInt-1
            for y in range(yInt-1,0,-1):
                checkSector = self.editSpace(x,y)
                if(checkSector in tableMap):
                    return x,y
                else:
                    if((x>1)and(y>1)):
                        x-=1
                    else:
                        return x,y
            return 1,1
        if (colType == "DR"):
            x=xInt+1
            for y in range(yInt-1,0,-1):
                checkSector = self.editSpace(x,y)
                if(checkSector in tableMap):
                    return x,y
                else:
                    if((x<8)and(y>1)):
                        x+=1
                    else:
                        return x,y
            return 8,1  
        return
    
    #D -> Diagonal    
    #H -> Horizontal or Vertical
    #R -> Restricted
    def setPlayType(self):
        if (self.typeChar=="P"):
            self.playType="R"         
        if (self.typeChar=="R"):
            self.playType="H"     
        if (self.typeChar=="N"):
            self.playType="R"      
        if (self.typeChar=="B"):
            self.playType="D"        
        if (self.typeChar=="Q"):
            self.playType="DH"        
        if (self.typeChar=="K"):
            self.playType="R"
        return None
        
    def availableMoves(self,tableMap):
        playTypes = list(self.playType)
        availableMoves = list()
        if("D" in playTypes):
            availableMoves.extend(self.calcDiagonalMoves(tableMap))
        if("H" in playTypes):
            availableMoves.extend(self.calcLinearMoves(tableMap))
        if(self.typeChar=="P"):
            availableMoves.extend(self.pawnMoves(tableMap))
            availableMoves.extend(self.pawnOt(tableMap))
        if(self.typeChar=="K"):
            availableMoves.extend(self.kingMoves(tableMap))
        if(self.typeChar=="N"):
            availableMoves.extend(self.knightMoves(tableMap))
        return availableMoves
    
    def calcLinearMoves(self,tableMap):
        linMovs = list()
        sectorSplit = list(self.space)
        xPos = self.xFrmKey[sectorSplit[0]]
        yPos = int(sectorSplit[1])
        for x in range(xPos+1, self.collisionDetection("R",tableMap)):
            if(self.freeSpace((self.xToKey[x] + str(yPos)),tableMap) == True):
                linMovs.append(self.editSpace(x,yPos))
            else:
                break
        for x in range(xPos-1,self.collisionDetection("L",tableMap), -1):
            if(self.freeSpace((self.xToKey[x] + str(yPos)),tableMap) == True):
                linMovs.append(self.editSpace(x,yPos))
            else:
                break
        for y in range(yPos+1, self.collisionDetection("U",tableMap)):
            if(self.freeSpace((sectorSplit[0]+str(y)),tableMap) == True):   
                linMovs.append(self.editSpace(xPos,y))
            else:
                break   
        for y in range(yPos-1,self.collisionDetection("D",tableMap),-1):
            if(self.freeSpace((sectorSplit[0]+str(y)),tableMap) == True): 
                linMovs.append(self.editSpace(xPos,y))
            else:
                break 
        return linMovs
    
    def calcDiagonalMoves(self,tableMap):
        dMovs = list()
        sectorSplit = list(self.space)
        xPos = self.xFrmKey[sectorSplit[0]]
        yPos = int(sectorSplit[1])
        xInt, yInt = self.collisionDetection("UL",tableMap)
        y=yPos
        for x in range(xPos,xInt-1,-1):
            if(y>8):
                break
            else:
                if(self.freeSpace(self.editSpace(x,y),tableMap) == True):
                    dMovs.append(self.editSpace(x,y))
                y+=1     
        xInt, yInt = self.collisionDetection("UR",tableMap)
        y=yPos
        for x in range(xPos,xInt+1):
            if(y>8):
                break
            else:
                if(self.freeSpace(self.editSpace(x,y),tableMap) == True):
                    dMovs.append(self.editSpace(x,y))
                y+=1
        xInt, yInt = self.collisionDetection("DR",tableMap)
        y=yPos
        for x in range(xPos,xInt+1):
            if(y<1):
                break
            else:
                if(self.freeSpace(self.editSpace(x,y),tableMap) == True):
                    dMovs.append(self.editSpace(x,y))
                y-=1
        xInt, yInt = self.collisionDetection("DL",tableMap)
        y=yPos
        for x in range(xPos,xInt-1,-1):
            if(y<1):
                break
            else:
                if(self.freeSpace(self.editSpace(x,y),tableMap) == True):
                    dMovs.append(self.editSpace(x,y))
                y-=1
        return dMovs
    
    def pawnMoves(self,tableMap):
        pawnMoves = list()
        sectorSplit = list(self.space)
        xPos = self.xFrmKey[sectorSplit[0]]
        yPos = int(sectorSplit[1])
        if(self.holder == "W"):
            pawnMulti = 1
        else:
            pawnMulti = -1
        if(self.freeSpace((sectorSplit[0]+str(yPos+pawnMulti)),tableMap) == True):
            pawnMoves.append(self.editSpace(0,pawnMulti+yPos))
            if(self.firstTurn == True):
                if((self.freeSpace((sectorSplit[0]+str(yPos+(2*pawnMulti))),tableMap)) == True):
                    pawnMoves.append(self.editSpace(0,(2*pawnMulti)+yPos))
        return pawnMoves

                    
    def kingMoves(self,tableMap):
        kingMoves = list()
        sectorSplit = list(self.space)
        xPos = self.xFrmKey[sectorSplit[0]]
        yPos = int(sectorSplit[1])
        diagonalMultipliers = [(1,1),(-1,-1),(1,-1),(-1,1)]
        kingAdd = [(1,0),(0,1),(-1,0),(0,-1)]
        for each in diagonalMultipliers:
            for x in range(1,2):
                checkX = xPos+(x*each[0])
                checkY = yPos+(x*each[1])
                if((0<checkX<9) and (0<checkY<9)):
                    if(self.freeSpace((self.xToKey[checkX]+str(checkY)), tableMap) == True):
                        kingMoves.append(self.editSpace(checkX,checkY))
        for each in kingAdd:
            curX = xPos + each[0]
            curY = yPos + each[1]
            if((0<curX<9) and (0<curY<9)):
                if(self.freeSpace((self.xToKey[curX]+str(curY)),tableMap) == True):
                    kingMoves.append(self.editSpace(curX, curY))
        return kingMoves

    def knightMoves(self,tableMap):
        knightMoves = list()
        sectorSplit = list(self.space)
        xPos = self.xFrmKey[sectorSplit[0]]
        yPos = int(sectorSplit[1])
        diagonalMultipliers = [(1,1),(-1,-1),(1,-1),(-1,1)]
        for each in diagonalMultipliers:
            curX = (xPos+(1*each[0]))
            curY = (yPos+(2*each[1]))
            if((0<curX<9) and (0<curY<9)):
                if(self.freeSpace((self.xToKey[curX]+str(curY)),tableMap) == True):
                    knightMoves.append(self.editSpace(curX,curY))
            curX = (xPos+(2*each[0]))
            curY = (yPos+(1*each[1]))
            if((0<curX<9) and (0<curY<9)):
                if(self.freeSpace((self.xToKey[curX]+str(curY)),tableMap) == True):
                    knightMoves.append(self.editSpace(curX,curY))   
        return knightMoves
