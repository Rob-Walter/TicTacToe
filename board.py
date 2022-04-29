from numbers import Number
from field import Field
from pawn import Pawn
from customEvents import playerMoved, createWinEvent, createDrawEvent, createImmobilizeEvent
import pygame
import globals

class Board:

    WHITE = (255,255,255)
    BLACK = (0,0,0)
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.surface = pygame.Surface((self.width, self.height))
        self.tempPawnSurface = None
        self.rows = 6
        self.columns = 6
        self.fieldArray2D = []
        for columnIndex in range(0,self.columns):
            column = []
            for rowIndex in range(0,self.rows):
                if(columnIndex % 2 == 0):
                    if (rowIndex % 2 == 0):
                        fieldColor = self.WHITE
                    else:
                        fieldColor = self.BLACK          
                else:
                    if (rowIndex % 2 == 0):
                        fieldColor = self.BLACK
                    else:
                        fieldColor = self.WHITE
                column.append(Field(((self.width / self.rows) * rowIndex), ((self.height / self.columns) * columnIndex),(self.width / self.rows),(self.height / self.columns),fieldColor))
            self.fieldArray2D.append(column)
        self.initializeNewGame()


    def get2dArray(self):
        return self.fieldArray2D

    def initializeNewGame(self):
        whitePlayerColumn = self.fieldArray2D[0]
        for field in whitePlayerColumn:
            field.addPawn(Pawn("white", field.getPosition()[0],field.getPosition()[1]))
        
        blackPlayerColumn = self.fieldArray2D[self.columns - 1]
        for field in blackPlayerColumn:
            field.addPawn(Pawn("black", field.getPosition()[0],field.getPosition()[1]))

    def moveMouse(self, event, currentTurnPlayer):
        for column in self.fieldArray2D:
            for field in column:
                if (field.isPawnCurrentlyDragged() == False):
                    field.checkMouseHover(event, currentTurnPlayer)
                else:
                    self.tempPawnSurface = (field.getPawn().draw(),(event.pos[0] - globals.boardStartingPointX - field.getPawn().getSize()[0] / 2, event.pos[1] - globals.boardStartingPointY - field.getPawn().getSize()[1] / 2))
                    


    def mousePressed(self, event, currentTurnPlayer):
        currentField = None
        for columnIndex, column in enumerate(self.fieldArray2D):
            for rowIndex, field in enumerate(column):
                if(field.isCurrentlyHovered()):
                    currentField = field
                    result =  self.checkPossibleMoves(columnIndex, rowIndex, currentTurnPlayer.getTeam())
                    print(result)
                    if result[0]:
                        self.markPossibleMove(result[0][0])
                    if result[1]:
                        self.markPossibleBeats(result[1])
                    field.startDraggingAndPassSurface(self.surface)
                    self.tempPawnSurface = (field.getPawn().draw(),(event.pos[0] - globals.boardStartingPointX - field.getPawn().getSize()[0] / 2, event.pos[1] - globals.boardStartingPointY - field.getPawn().getSize()[1] / 2))
        


    def markPossibleMove(self, movePosition):
        self.fieldArray2D[movePosition[0]][movePosition[1]].markAsPossibleMove(True)
    
    def markPossibleBeats(self, beatPositions):
        for position in beatPositions:
            self.fieldArray2D[position[0]][position[1]].markAsPossibleBeat(True)

    def checkPossibleMoves(self, column, row,  team):
        possibleMove = []
        possibleBeats = []
        result = []
        if (team == "white" ):
            if (column  < self.columns - 1): 
                if(self.fieldArray2D[column+1][row].getPawn() == None):
                    possibleMove.append((column + 1, row))
                if (row > 0):
                    if (self.fieldArray2D[column+1][row - 1].getPawn() != None and self.fieldArray2D[column+1][row - 1].getPawn().getTeam() == "black"):
                        possibleBeats.append((column + 1, row - 1))
                if (row < self.rows - 1):
                       if (self.fieldArray2D[column+1][row + 1].getPawn() != None and self.fieldArray2D[column+1][row + 1].getPawn().getTeam() == "black"):
                        possibleBeats.append((column + 1, row + 1))
        elif(team == "black"):
            if (column  > 0): 
                if(self.fieldArray2D[column - 1][row].getPawn() == None):
                    possibleMove.append((column - 1, row))
                if (row > 0):
                    if (self.fieldArray2D[column - 1][row - 1].getPawn() != None and self.fieldArray2D[column - 1][row - 1].getPawn().getTeam() == "white"):
                        possibleBeats.append((column - 1, row - 1))
                if (row < self.rows - 1):
                       if (self.fieldArray2D[column - 1][row + 1].getPawn() != None and self.fieldArray2D[column - 1][row + 1].getPawn().getTeam() == "white"):
                        possibleBeats.append((column - 1, row + 1))
        result.append(possibleMove)
        result.append(possibleBeats)
        return result

    def mouseReleased(self,event, currentTurnPlayer):
        oldField = None
        newField = None
        for columnIndex, column in enumerate(self.fieldArray2D):
            for rowIndex, field in enumerate(column):
                if(field.isMarkedAsPossibleMove()):
                    if(field.checkDraggedPawnHover(event)):
                        newField = field
                    field.markAsPossibleMove(False)
                if(field.isMarkedAsPossiblebeat()):
                    if(field.checkDraggedPawnHover(event)):
                        newField = field
                    field.markAsPossibleBeat(False)
                if(field.isPawnCurrentlyDragged()):
                    oldField = field
                    field.stopDraggingAndDeleteSurface()
                    self.tempPawnSurface = None
                if(field.isCurrentlyHovered()):
                    field.markAsHovered(False)
        if(oldField and newField):
            newField.addPawn(oldField.getPawn())
            oldField.removePawn()
            self.checkForWinOrDraw()
            pygame.event.post(playerMoved)
       

    def checkForWinOrDraw(self):
        playerWhitePawnCount = 0
        playerBlackPawnCount = 0
        playerWhitePossibleMoves = 0
        playerBlackPossibleMoves = 0
        for columnIndex, column in enumerate(self.fieldArray2D):
            for rowIndex, field in enumerate(column):
                if(field.getPawn() != None):
                    pawn = field.getPawn()
                    if(pawn.getTeam() == "white"):
                        if(columnIndex == self.columns - 1):
                            pygame.event.post(createWinEvent("white"))
                            return
                        playerWhitePawnCount += 1
                        checkMoves = self.checkPossibleMoves(columnIndex, rowIndex, pawn.getTeam())
                        if(checkMoves[0] or checkMoves[1]):
                            playerWhitePossibleMoves += 1
                    elif(pawn.getTeam() == "black"):
                        if(columnIndex == 0):
                             pygame.event.post(createWinEvent("black"))
                             return
                        playerBlackPawnCount += 1
                        checkMoves = self.checkPossibleMoves(columnIndex, rowIndex, pawn.getTeam())
                        if(checkMoves[0] or checkMoves[1]):
                            playerBlackPossibleMoves += 1
        if(playerWhitePawnCount == 0):
            pygame.event.post(createWinEvent("black"))
        elif(playerBlackPawnCount == 0):
            pygame.event.post(createWinEvent("white"))
        if(playerWhitePossibleMoves == 0):
            pygame.event.post(createImmobilizeEvent("white"))
        if(playerBlackPossibleMoves == 0):
            pygame.event.post(createImmobilizeEvent("black"))
        if(playerWhitePossibleMoves == 0 and playerBlackPossibleMoves == 0):
            pygame.event.post(createDrawEvent())
        

    def draw(self):
        for columnIndex,column in enumerate(self.fieldArray2D):
            for rowIndex, field in enumerate(column):  
                self.surface.blit(field.draw(), field.getPosition())
        if(self.tempPawnSurface):
            self.surface.blit(self.tempPawnSurface[0] ,self.tempPawnSurface[1])
        return self.surface

    def evaluate(self):
        countBlack:int = 0
        countWhite:int = 0
        score :int = 0
        for rowIndex, column in enumerate(self.fieldArray2D):
            for columnIndex, field in enumerate(column):
                if field.getPawn() is not None:                
                    if(field.getPawn().team == "black"):
                        if(columnIndex == self.columns - 1):
                            return float('inf')
                        countBlack += 1
                        countBlack +=   (-(rowIndex -5)) * 10
                    if(field.getPawn().team == "white"):
                        if(columnIndex == self.columns - 1):
                            return float('-inf')
                        countWhite += 1 
                        countWhite +=  rowIndex * 10
        score = countBlack - countWhite
        return score

    def get_all_pices(self, color):
        allPices=[]
        for rowIndex, column in enumerate(self.fieldArray2D):
            for columnIndex, field in enumerate(column):
                if field.getPawn() is not None:                
                    if(field.getPawn().team == color):
                        allPices.append([rowIndex, columnIndex])
        return allPices
    
    def checkPossibleMovesComp(self, column, row,  currentTurnPlayer):
        possibleMove = []
        possibleBeats = []
        result = []
        if (currentTurnPlayer == "white" ):
            if (column  < self.columns - 1): 
                if(self.fieldArray2D[column+1][row].getPawn() == None):
                    possibleMove.append((column + 1, row))
                if (row > 0):
                    if (self.fieldArray2D[column+1][row - 1].getPawn() != None and self.fieldArray2D[column+1][row - 1].getPawn().getTeam() == "black"):
                        possibleBeats.append((column + 1, row - 1))
                if (row < self.rows - 1):
                       if (self.fieldArray2D[column+1][row + 1].getPawn() != None and self.fieldArray2D[column+1][row + 1].getPawn().getTeam() == "black"):
                        possibleBeats.append((column + 1, row + 1))
        elif(currentTurnPlayer == "black"):
            if (column  > 0): 
                if(self.fieldArray2D[column - 1][row].getPawn() == None):
                    possibleMove.append((column - 1, row))
                if (row > 0):
                    if (self.fieldArray2D[column - 1][row - 1].getPawn() != None and self.fieldArray2D[column - 1][row - 1].getPawn().getTeam() == "white"):
                        possibleBeats.append((column - 1, row - 1))
                if (row < self.rows - 1):
                       if (self.fieldArray2D[column - 1][row + 1].getPawn() != None and self.fieldArray2D[column - 1][row + 1].getPawn().getTeam() == "white"):
                        possibleBeats.append((column - 1, row + 1))
        result.append(possibleMove)
        result.append(possibleBeats)
        return result

    
    def move(self,piece,move):
        print("move",move)
        print("piece",piece)
        tempPawn=self.fieldArray2D[piece[0]][piece[1]].getPawn()
        self.fieldArray2D[move[0]][move[1]].addPawn(tempPawn) 
        self.fieldArray2D[piece[0]][piece[1]].removePawn()


