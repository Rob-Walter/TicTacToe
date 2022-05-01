from xml.dom.minidom import Element
import globals
import pygame
import pygame_gui
from pygame_gui.core import ObjectID

def createButton(pos, text, type ,manager):
    return pygame_gui.elements.UIButton(relative_rect=pygame.Rect(pos, (130, 50)), text=text, manager=manager, object_id=ObjectID(class_id=type))

def createInput(pos, type,manager):
    element = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(pos, (130, 50)), manager=manager, object_id=ObjectID(class_id=type))
    if type == globals.inputTypes['PASSWORD']:    
        element.set_text_hidden(True)
    return element

def createTextfeld(pos, text, type, manager):
    if type == globals.textboxTypes['INFO']:
        element = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(pos, (130, 50)), html_text=text, manager=manager, object_id=ObjectID(class_id=type))
    elif type == globals.textboxTypes['RULES']:
        element = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(pos, (900, 500)), html_text=text, manager=manager, object_id=ObjectID(class_id=type))
    elif type == globals.textboxTypes['SAVE']:
        element = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(pos, (250, 50)), html_text=text, manager=manager, object_id=ObjectID(class_id=type))
    elif type == globals.textboxTypes['DATA']:
        element = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(pos, (100, 50)), html_text=text, manager=manager, object_id=ObjectID(class_id=type))
    #element.rebuild()
    #element.full_redraw()
    return element

def createdropwdown(pos, optionslist, starting_option, manager):
    element = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(pos, (100, 50)),options_list=optionslist, starting_option=starting_option, manager=manager)
    return element
