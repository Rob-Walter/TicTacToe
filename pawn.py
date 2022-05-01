import pygame
import os

class Pawn:

    WIDTH, HEIGHT = 70 ,70

    def __init__(self,team,x : int,y : int):
        self.team = team
        self.width = self.WIDTH
        self.height = self.HEIGHT
        self.x = x
        self.y = y
        self.setSprite()


    def getSize(self):
        return (self.width, self.height)

    def getTeam(self):
        return self.team
        
    def draw(self):
        return self.sprite
    
    def setSprite(self):
        if(self.team == "white"):
            self.sprite = pygame.image.load(os.path.join("assets", "circle.png"))
        elif(self.team == "black"):
            self.sprite = pygame.image.load(os.path.join("assets", "cross.png"))
        self.sprite = pygame.transform.scale(self.sprite, self.getSize())

    def unsetSprite(self):
        self.sprite = None