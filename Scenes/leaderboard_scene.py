from array import array
from audioop import reverse
from shelve import DbfilenameShelf
import Scenes.mainmenue_scene
import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
from database_controller import DB_Controller




class LeaderboardScene(Scene):
    #GUI Manager
    def __init__(self):
        self.leader_manager = pygame_gui.UIManager((1200, 800), 'theme.json')
        self.back_button = gui_elements.createButton((0,350),'BACK',globals.buttonTypes['ACCEPT'], self.leader_manager)
        self.currentleaderboardarray = []
        self.currentUiElements = []
        #self.rules_label = gui_elements.createTextfeld((200,150),"text",globals.textboxTypes['RULES'], self.leader_manager)

        self.easy_button = gui_elements.createButton((300,50),'EASY',globals.buttonTypes['STRENGTH'], self.leader_manager)
        self.medium_button = gui_elements.createButton((450,50),'MEDIUM',globals.buttonTypes['STRENGTH'], self.leader_manager)
        self.hard_button = gui_elements.createButton((600,50),'HARD',globals.buttonTypes['STRENGTH'], self.leader_manager)

    def update(self, time_delta):
        self.leader_manager.update(time_delta)

    def render(self, screen):
        self.leader_manager.draw_ui(screen)

    def getleaderboard(self, ki_strength):
        dbcontroller = DB_Controller()
        leaderboard = dbcontroller.getallleaderboard(ki_strength)
        self.currentleaderboardarray = self.sortleaderboard(leaderboard)
        self.drawleaderboard()
        #print(ausgabe)
    
    def sortleaderboard(self, leaderboard):
        ausgabe = []
        for entry in leaderboard:
            if not [item for item in ausgabe if item[0] == entry[0]]:
                ausgabe.append(list(entry))
            else:
                for element in ausgabe:
                    if element[0] == entry[0]:
                        element[1] += entry[1]
                        element[2] += entry[2]
        ausgabe.sort(key=lambda x:int(x[1]), reverse=True)
        return ausgabe
    
    def drawleaderboard(self):

        offset_y = 250
        offset_x = 350

        for uiElement in self.currentUiElements:
            uiElement.kill()

        self.currentUiElements = []

        self.currentUiElements.append(gui_elements.createTextfeld((offset_x,offset_y-50),'USERNAME',globals.textboxTypes['DATA'], self.leader_manager))
        self.currentUiElements.append(gui_elements.createTextfeld((offset_x+100,offset_y-50),'WINS',globals.textboxTypes['DATA'], self.leader_manager))
        self.currentUiElements.append(gui_elements.createTextfeld((offset_x+100*2,offset_y-50),'LOSSES',globals.textboxTypes['DATA'], self.leader_manager))


        for index,element in enumerate(self.currentleaderboardarray):
            result = element[0]+":"+str(element[1])+" / "+str(element[2])
            #print(result)
            self.currentUiElements.append(gui_elements.createTextfeld((offset_x,offset_y+50*index),element[0],globals.textboxTypes['DATA'], self.leader_manager))
            self.currentUiElements.append(gui_elements.createTextfeld((offset_x+100,offset_y+50*index),str(element[1]),globals.textboxTypes['DATA'], self.leader_manager))
            self.currentUiElements.append(gui_elements.createTextfeld((offset_x+100*2,offset_y+50*index),str(element[2]),globals.textboxTypes['DATA'], self.leader_manager))



    def handleEvents(self, events):
        for event in events:
            self.leader_manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.back_button:
                                print('back')
                                self.manager.goTo(Scenes.mainmenue_scene.MainMenueScene())
                            elif event.ui_element == self.easy_button:
                                print('leaderboard for easy')
                                self.getleaderboard('EASY')
                            elif event.ui_element == self.medium_button:
                                print('leaderboard for medium')
                                self.getleaderboard('MEDIUM')
                            elif event.ui_element == self.hard_button:
                                print('leaderboard for hard')
                                self.getleaderboard('HARD')
                    #if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED: 
                        #if event.ui_element == self.username_input:
                            #username = self.username_input.get_text()
                            #print('text:', username)