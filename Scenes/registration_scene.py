import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
#from Scenes.login_scene import LoginScene
import Scenes.start_scene
import Scenes.login_scene

from database_controller import DB_Controller




class RegistrationScene(Scene):
    #GUI Manager
    def __init__(self):
        self.username = ""
        self.password = ""
        
        self.registration_manager = pygame_gui.UIManager((1200, 800), 'theme.json')

        self.login_label = gui_elements.createTextfeld((500,200),'NEW USERNAME',globals.textboxTypes['INFO'], self.registration_manager)
        self.username_input = gui_elements.createInput((500,250),globals.inputTypes['NORMAL'], self.registration_manager)

        self.password_label = gui_elements.createTextfeld((500,320),'NEW PASSWORD',globals.textboxTypes['INFO'], self.registration_manager)
        self.password_input = gui_elements.createInput((500,370),globals.inputTypes['PASSWORD'], self.registration_manager)

        self.registration_button = gui_elements.createButton((500,480),'REGISTER',globals.buttonTypes['ACCEPT'], self.registration_manager)

        self.back_button = gui_elements.createButton((500,530),'BACK',globals.buttonTypes['ACCEPT'], self.registration_manager)

    def register(self):
        dbcontroller = DB_Controller()
        return dbcontroller.insertnewplayer(self.username, self.password)

    def update(self, time_delta):
        self.registration_manager.update(time_delta)

    def render(self, screen):
        self.registration_manager.draw_ui(screen)

    def handleEvents(self, events):
        for event in events:
            self.registration_manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.registration_button:
                            self.username = self.username_input.get_text()
                            self.password = self.password_input.get_text()
                            if len(self.username) >= 3 and len(self.password)  >= 3:
                                if self.register():
                                    #bitte weiterleiten auf login_scene
                                    self.manager.goTo(Scenes.login_scene.LoginScene())
                            else:
                                print('bitte längere Eingabe machen')
                        elif event.ui_element == self.back_button:
                            print('back')
                            self.manager.goTo(Scenes.start_scene.StartScene())
                    elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED: 
                        if event.ui_element == self.username_input:
                            username = self.username_input.get_text()
                            print('text:', username)