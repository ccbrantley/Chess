import chessPiece
class table:
    tableMap = {"A1" : ['R','W'], "H1" : ['R','W'],
           "B1" : ['N','W'], "G1" : ['N','W'],
           "C1" : ['B','W'], "F1" : ['B','W'],
           "D1" : ['Q','W'], "E1" : ['K','W'],
           
           "A2" : ['P','W'], "H2" : ['P','W'],
           "B2" : ['P','W'], "G2" : ['P','W'],
           "C2" : ['P','W'], "F2" : ['P','W'],
           "D2" : ['P','W'], "E2" : ['P','W'],

           "A3" : ['',''], "H3" : ['',''],
           "B3" : ['',''], "G3" : ['',''],
           "C3" : ['',''], "F3" : ['',''],
           "D3" : ['',''], "E3" : ['',''],

           "A4" : ['',''], "H4" : ['',''],
           "B4" : ['',''], "G4" : ['',''],
           "C4" : ['',''], "F4" : ['',''],
           "D4" : ['',''], "E4" : ['',''],

           "A5" : ['',''], "H5" : ['',''],
           "B5" : ['',''], "G5" : ['',''],
           "C5" : ['',''], "F5" : ['',''],
           "D5" : ['',''], "E5" : ['',''],

           "A6" : ['',''], "H6" : ['',''],
           "B6" : ['',''], "G6" : ['',''],
           "C6" : ['',''], "F6" : ['',''],
           "D6" : ['',''], "E6" : ['',''],

           "A7" : ['P','X'], "H7" : ['P','X'],
           "B7" : ['P','X'], "G7" : ['P','X'],
           "C7" : ['P','X'], "F7" : ['P','X'],
           "D7" : ['P','X'], "E7" : ['P','X'],

           "A8" : ['R','X'], "H8" : ['R','X'],
           "B8" : ['N','X'], "G8" : ['N','X'],
           "C8" : ['B','X'], "F8" : ['B','X'],
           "D8" : ['Q','X'], "E8" : ['K','X']
           }
    tableMapTest = {}
    def __init__(self):
        self.playerTurn = "W"
    
    def getShapeType(self, spaceCheck):
        imageNames = {'N' : "knightBA.gif", 'B' : "bishopBA.gif",
                      'Q' : "queenBA.gif", 'K' : "kingBA.gif",
                      'P' : "pawnBA.gif", 'R' : "rookBA.gif"}
        return imageNames[spaceCheck[0]]
    
    def updateTable(self, keySpace, chessPiece):
        self.tableMapTest[keySpace] = chessPiece
    def getPlayerTurn(self):
        return self.playerTurn
    
    def updatePlayerTurn(self, player):
        self.playerTurn = player
        
        
        
    
    
