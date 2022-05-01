from numbers import Number
from xmlrpc.client import boolean
from field import Field
from pawn import Pawn
from customEvents import playerMoved, createWinEvent, createDrawEvent, createImmobilizeEvent
import pygame

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
        #self.initializeNewGame()


    def get2dArray(self):
        return self.fieldArray2D

    # def initializeNewGame(self):
    #     whitePlayerColumn = self.fieldArray2D[0]
    #     for field in whitePlayerColumn:
    #         field.addPawn(Pawn("white", field.getPosition()[0],field.getPosition()[1]))
        
    #     blackPlayerColumn = self.fieldArray2D[self.columns - 1]
    #     for field in blackPlayerColumn:
    #         field.addPawn(Pawn("black", field.getPosition()[0],field.getPosition()[1]))

    def moveMouse(self, event, currentTurnPlayer):
        for column in self.fieldArray2D:
            for field in column:
                field.checkMouseHover(event, currentTurnPlayer)
               

    def mousePressed(self, event, currentTurnPlayer):
        currentField = None
        for columnIndex, column in enumerate(self.fieldArray2D):
            for rowIndex, field in enumerate(column):
                if(field.isCurrentlyHovered()):
                    currentField = field
                    result =  self.checkPossibleMoves(columnIndex, rowIndex)
                    print("result",result)
                    if result:
                        currentField.addPawn(Pawn(currentTurnPlayer.getTeam() , field.getPosition()[0] , field.getPosition()[1]))
                        self.checkForWinOrDraw()
                        pygame.event.post(playerMoved)
                       
        


    # def markPossibleMove(self, movePosition):
    #     self.fieldArray2D[movePosition[0]][movePosition[1]].markAsPossibleMove(True)
    
    # def markPossibleBeats(self, beatPositions):
    #     for position in beatPositions:
    #         self.fieldArray2D[position[0]][position[1]].markAsPossibleBeat(True)

    def checkPossibleMoves(self, column, row):
        if(self.fieldArray2D[column][row].getPawn() == None):
            return column, row
        return []

    # def mouseReleased(self,event, currentTurnPlayer):
    #     oldField = None
    #     newField = None
    #     for columnIndex, column in enumerate(self.fieldArray2D):
    #         for rowIndex, field in enumerate(column):
    #             if(field.isMarkedAsPossibleMove()):
    #                 if(field.checkDraggedPawnHover(event)):
    #                     newField = field
    #                 field.markAsPossibleMove(False)
    #             if(field.isMarkedAsPossiblebeat()):
    #                 if(field.checkDraggedPawnHover(event)):
    #                     newField = field
    #                 field.markAsPossibleBeat(False)
    #             if(field.isPawnCurrentlyDragged()):
    #                 oldField = field
    #                 field.stopDraggingAndDeleteSurface()
    #                 self.tempPawnSurface = None
    #             if(field.isCurrentlyHovered()):
    #                 field.markAsHovered(False)
    #     if(oldField and newField):
    #         newField.addPawn(oldField.getPawn())
    #         oldField.removePawn()
    #         self.checkForWinOrDraw()
    #         pygame.event.post(playerMoved)
       

    def checkForWinOrDraw(self, isSimulated = False):
        emptyField = 0
        for columnIndex, column in enumerate(self.fieldArray2D):
            for rowIndex, field in enumerate(column):
                if(field.getPawn() == None):
                    emptyField += 1
                else:
                    pawn = field.getPawn()  
                    color =pawn.getTeam() 
                    if(rowIndex<3):
                        first:boolean = False
                        second: boolean = False
                        third: boolean = False
                        if(self.fieldArray2D[columnIndex][rowIndex+1].getPawn()):
                            if(self.fieldArray2D[columnIndex][rowIndex+1].getPawn().getTeam() ==color):
                                first = True
                        if(self.fieldArray2D[columnIndex][rowIndex+2].getPawn()):
                            if(self.fieldArray2D[columnIndex][rowIndex+2].getPawn().getTeam() ==color):
                                second = True
                        if(self.fieldArray2D[columnIndex][rowIndex+3].getPawn()):
                            if(self.fieldArray2D[columnIndex][rowIndex+3].getPawn().getTeam() ==color):
                                third = True               
                        if(first and second and third):
                            if not isSimulated:
                                pygame.event.post(createWinEvent(color))
                                return
                            return ("win", color)
                    if(columnIndex < 3):
                        first:boolean = False
                        second: boolean = False
                        third: boolean = False
                        if(self.fieldArray2D[columnIndex+1][rowIndex].getPawn()):
                            if(self.fieldArray2D[columnIndex+1][rowIndex].getPawn().getTeam() ==color):
                                first = True
                        if(self.fieldArray2D[columnIndex+2][rowIndex].getPawn()):
                            if(self.fieldArray2D[columnIndex+2][rowIndex].getPawn().getTeam() ==color):
                                second = True
                        if(self.fieldArray2D[columnIndex+3][rowIndex].getPawn()):
                            if(self.fieldArray2D[columnIndex+3][rowIndex].getPawn().getTeam() ==color):
                                third = True               
                        if(first and second and third):
                            if not isSimulated:
                                pygame.event.post(createWinEvent(color))
                                return
                            return ("win", color)
                    if(rowIndex<3 and columnIndex <3):
                        first:boolean = False
                        second: boolean = False
                        third: boolean = False
                        if(self.fieldArray2D[columnIndex+1][rowIndex+1].getPawn()):
                            if(self.fieldArray2D[columnIndex+1][rowIndex+1].getPawn().getTeam() ==color):
                                first = True
                        if(self.fieldArray2D[columnIndex+2][rowIndex+2].getPawn()):
                            if(self.fieldArray2D[columnIndex+2][rowIndex+2].getPawn().getTeam() ==color):
                                second = True
                        if(self.fieldArray2D[columnIndex+3][rowIndex+3].getPawn()):
                            if(self.fieldArray2D[columnIndex+3][rowIndex+3].getPawn().getTeam() ==color):
                                third = True               
                        if(first and second and third):
                            if not isSimulated:
                                pygame.event.post(createWinEvent(color))
                                return
                            return ("win", color)

                    if(rowIndex>2 and columnIndex <3):
                        first:boolean = False
                        second: boolean = False
                        third: boolean = False
                        if(self.fieldArray2D[columnIndex+1][rowIndex-1].getPawn()):
                            if(self.fieldArray2D[columnIndex+1][rowIndex-1].getPawn().getTeam() ==color):
                                first = True
                        if(self.fieldArray2D[columnIndex+2][rowIndex-2].getPawn()):
                            if(self.fieldArray2D[columnIndex+2][rowIndex-2].getPawn().getTeam() ==color):
                                second = True
                        if(self.fieldArray2D[columnIndex+3][rowIndex-3].getPawn()):
                            if(self.fieldArray2D[columnIndex+3][rowIndex-3].getPawn().getTeam() ==color):
                                third = True               
                        if(first and second and third):
                            if not isSimulated:
                                pygame.event.post(createWinEvent(color))
                                return
                            return ("win", color)
        if emptyField == 0:
            if not isSimulated:
                pygame.event.post(createWinEvent(color))
                return
            return ("draw","")
        return("","")
        

    def draw(self):
        for columnIndex,column in enumerate(self.fieldArray2D):
            for rowIndex, field in enumerate(column):  
                self.surface.blit(field.draw(), field.getPosition())
        if(self.tempPawnSurface):
            self.surface.blit(self.tempPawnSurface[0] ,self.tempPawnSurface[1])
        return self.surface

    def evaluate(self):
        twoInARowValue = 10000.0
        threeInARowValue = 25000.0
        fourInARowValue = 40000.0
        countWhite:int = 0
        score :int = 0
        for columnIndex, column in enumerate(self.fieldArray2D):
            for rowIndex, field in enumerate(column):
                if(field.getPawn() != None):
                    pawn = field.getPawn()
                    color = pawn.getTeam()
                    if(rowIndex<3):
                        first:boolean = False
                        second: boolean = False
                        third: boolean = False
                        if(self.fieldArray2D[columnIndex][rowIndex+1].getPawn()):
                            if(self.fieldArray2D[columnIndex][rowIndex+1].getPawn().getTeam() ==color):
                                first = True
                        if(self.fieldArray2D[columnIndex][rowIndex+2].getPawn()):
                            if(self.fieldArray2D[columnIndex][rowIndex+2].getPawn().getTeam() ==color):
                                second = True
                        if(self.fieldArray2D[columnIndex][rowIndex+3].getPawn()):
                            if(self.fieldArray2D[columnIndex][rowIndex+3].getPawn().getTeam() ==color):
                                third = True               
                        if(first and second and third):
                            if(color == "white"):
                                score += -fourInARowValue
                            if(color == "black"):
                                score += fourInARowValue
                        elif (first and second):
                            if(color == "white"):
                                score += -threeInARowValue
                            if(color == "black"):
                                score += threeInARowValue
                        elif(first):
                            if(color == "white"):
                                score += -twoInARowValue
                            if(color == "black"):
                                score += twoInARowValue

                    if(columnIndex < 3):
                        first:boolean = False
                        second: boolean = False
                        third: boolean = False
                        if(self.fieldArray2D[columnIndex+1][rowIndex].getPawn()):
                            if(self.fieldArray2D[columnIndex+1][rowIndex].getPawn().getTeam() ==color):
                                first = True
                        if(self.fieldArray2D[columnIndex+2][rowIndex].getPawn()):
                            if(self.fieldArray2D[columnIndex+2][rowIndex].getPawn().getTeam() ==color):
                                second = True
                        if(self.fieldArray2D[columnIndex+3][rowIndex].getPawn()):
                            if(self.fieldArray2D[columnIndex+3][rowIndex].getPawn().getTeam() ==color):
                                third = True               
                        if(first and second and third):
                            if(color == "white"):
                                score += -fourInARowValue
                            if(color == "black"):
                                score += fourInARowValue
                        elif (first and second):
                            if(color == "white"):
                                score += -threeInARowValue
                            if(color == "black"):
                                score += threeInARowValue
                        elif(first):
                            if(color == "white"):
                                score += -twoInARowValue
                            if(color == "black"):
                                score += twoInARowValue
                    if(rowIndex<3 and columnIndex <3):
                        first:boolean = False
                        second: boolean = False
                        third: boolean = False
                        if(self.fieldArray2D[columnIndex+1][rowIndex+1].getPawn()):
                            if(self.fieldArray2D[columnIndex+1][rowIndex+1].getPawn().getTeam() ==color):
                                first = True
                        if(self.fieldArray2D[columnIndex+2][rowIndex+2].getPawn()):
                            if(self.fieldArray2D[columnIndex+2][rowIndex+2].getPawn().getTeam() ==color):
                                second = True
                        if(self.fieldArray2D[columnIndex+3][rowIndex+3].getPawn()):
                            if(self.fieldArray2D[columnIndex+3][rowIndex+3].getPawn().getTeam() ==color):
                                third = True               
                        if(first and second and third):
                            if(color == "white"):
                                score += -fourInARowValue
                            if(color == "black"):
                                score += fourInARowValue
                        elif (first and second):
                            if(color == "white"):
                                score += -threeInARowValue
                            if(color == "black"):
                                score += threeInARowValue
                        elif(first):
                            if(color == "white"):
                                score += -twoInARowValue
                            if(color == "black"):
                                score += twoInARowValue

                    if(rowIndex>2 and columnIndex <3):
                        first:boolean = False
                        second: boolean = False
                        third: boolean = False
                        if(self.fieldArray2D[columnIndex+1][rowIndex-1].getPawn()):
                            if(self.fieldArray2D[columnIndex+1][rowIndex-1].getPawn().getTeam() ==color):
                                first = True
                        if(self.fieldArray2D[columnIndex+2][rowIndex-2].getPawn()):
                            if(self.fieldArray2D[columnIndex+2][rowIndex-2].getPawn().getTeam() ==color):
                                second = True
                        if(self.fieldArray2D[columnIndex+3][rowIndex-3].getPawn()):
                            if(self.fieldArray2D[columnIndex+3][rowIndex-3].getPawn().getTeam() ==color):
                                third = True               
                        if(first and second and third):
                            if(color == "white"):
                                score += -fourInARowValue
                            if(color == "black"):
                                score += fourInARowValue
                        elif (first and second):
                            if(color == "white"):
                                score += -threeInARowValue
                            if(color == "black"):
                                score += threeInARowValue
                        elif(first):
                            if(color == "white"):
                                score += -twoInARowValue
                            if(color == "black"):
                                score += twoInARowValue
        #score = countBlack - countWhite
        return score

   
    def get_all_pices(self, color):
        allPices=[]
        for rowIndex, column in enumerate(self.fieldArray2D):
            for columnIndex, field in enumerate(column):
                if field.getPawn() is not None:                
                    if(field.getPawn().team == color):
                        allPices.append([rowIndex, columnIndex])
        return allPices
    
    def checkPossibleMovesComp(self):
        possibleMove = []
        result = []
        for rowIndex, column in enumerate(self.fieldArray2D):
            for columnIndex, field in enumerate(column):
                if field.getPawn() is None:      
                    possibleMove.append((rowIndex,columnIndex))
        result.append(possibleMove)
        return result

    
    def move(self,move,color):
        #print("move",move)
        self.fieldArray2D[move[0]][move[1]].addPawn(Pawn(color,move[0],move[1]) )
        return



