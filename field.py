import pygame
import globals
from pygame import Surface
from pawn import Pawn

class Field:
    def __init__(self, x : int,y : int , width : int , height : int, color):
        self.pawn = None
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.isHovered = False
        self.isMovePossible = False
        self.isBeatPossible = False
        self.isDraggingPawn = False
        self.boardSurface = None
        self.setSurface()

    def addPawn(self,pawn : Pawn):
        self.pawn = pawn

    def removePawn(self):
        self.pawn = None

    def getPawn(self):
        return self.pawn

    def getPosition(self):
        return (self.x,self.y)

    def isCurrentlyHovered(self):
        return self.isHovered

    def markAsHovered(self, isTrue):
        self.isHovered = isTrue

    def isMarkedAsPossibleMove(self):
        return self.isMovePossible

    def markAsPossibleMove(self, isTrue):
        self.isMovePossible = isTrue

    def isMarkedAsPossiblebeat(self):
        return self.isBeatPossible

    def markAsPossibleBeat(self, isTrue):
        self.isBeatPossible = isTrue

    def isPawnCurrentlyDragged(self):
        return self.isDraggingPawn

    def isPawnGettingDragged(self, isTrue):
        self.isDraggingPawn = isTrue

    def startDraggingAndPassSurface(self, surface):
        self.boardSurface = surface
        self.isPawnGettingDragged(True)

    def stopDraggingAndDeleteSurface(self):
        self.boardSurface = None
        self.isPawnGettingDragged(False)

    def movePawnOnBoardSurface(self, position):
        if(self.boardSurface):
            self.boardSurface.blit(self.pawn.draw(),(position[0],position[1]))

    def checkMouseHover(self, event, currentTurnPlayer):
        if(self.pawn == None):
            if(self.surface.get_rect(topleft=((globals.boardStartingPointX + self.x),(globals.boardStartingPointY + self.y))).collidepoint(event.pos)):
                self.isHovered = True
            else:
                self.isHovered = False

    def checkDraggedPawnHover(self, event):
        if (self.surface.get_rect(topleft=((globals.boardStartingPointX + self.x),(globals.boardStartingPointY + self.y))).collidepoint(event.pos)):
            return True
        else:
            return False

    def draw(self):
        pygame.draw.rect(self.surface,self.color,pygame.Rect(0,0,self.width,self.height))
        pygame.draw.rect(self.surface,(self.color[0]-30,self.color[1]-30,self.color[2]-30),pygame.Rect(0,0,self.width,self.height), 3)
        if (self.isHovered == True):
            pygame.draw.rect(self.surface,globals.fieldHighLightColor,pygame.Rect(0,0,self.width,self.height), 3)
        if (self.isMovePossible == True):
            pygame.draw.rect(self.surface,globals.fieldPossibleMoveColor,pygame.Rect(0,0,self.width,self.height), 3)
        if (self.isBeatPossible == True):
            pygame.draw.rect(self.surface,globals.fieldPossibleBeatColor,pygame.Rect(0,0,self.width,self.height), 3)
        if(self.pawn != None and self.isDraggingPawn != True):
            self.surface.blit(self.pawn.draw(),(self.width / 2 - self.pawn.getSize()[0] / 2, self.height / 2 - self.pawn.getSize()[1] / 2))
        return self.surface

    def setSurface(self):
        self.surface = Surface((self.width,self.height))

    def unsetSurface(self):
        self.surface = None