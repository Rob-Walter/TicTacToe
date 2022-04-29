import pygame

PLAYERMOVED = 1
PLAYERWIN = 2
DRAW = 3
IMMOBILIZED = 4

playerMoved = pygame.event.Event(pygame.USEREVENT, {"customType":PLAYERMOVED})

def createWinEvent(winner):
    return pygame.event.Event(pygame.USEREVENT, {"customType":PLAYERWIN, "winner":winner})

def createDrawEvent():
    return pygame.event.Event(pygame.USEREVENT, {"customType":DRAW})

def createImmobilizeEvent(teamImmobilized):
    return pygame.event.Event(pygame.USEREVENT, {"customType":IMMOBILIZED, "immobilzedPlayer":teamImmobilized})
