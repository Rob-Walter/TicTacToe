import globals
import pygame
import pygame_gui
from pygame_gui.core import ObjectID

def createButton(pos, text, type ,manager):
    return pygame_gui.elements.UIButton(relative_rect=pygame.Rect(pos, (100, 50)), text=text, manager=manager, object_id=ObjectID(class_id=type))

def createInput(pos, type,manager):
    element = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(pos, (100, 50)), manager=manager, object_id=ObjectID(class_id=type))
    if type == globals.inputTypes['PASSWORD']:    
        element.set_text_hidden(True)
    return element

def createTextfeld(pos, text, type, manager):
    element = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(pos, (-1, -1)), html_text=text, manager=manager, object_id=ObjectID(class_id=type))
    element.rebuild()
    element.full_redraw()    
    return element