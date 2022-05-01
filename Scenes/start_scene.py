import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
import Scenes.game_Scene
import Scenes.start_scene
import Scenes.mainmenue_scene
from database_controller import DB_Controller

class StartScene(Scene):
    #GUI Manager
    def __init__(self):        
        self.startscene_manager = pygame_gui.UIManager((1200, 800), 'theme.json')

        self.guest_button = gui_elements.createButton((500,350),'GUEST',globals.buttonTypes['ACCEPT'], self.startscene_manager)
        self.login_button = gui_elements.createButton((500,400),'LOGIN',globals.buttonTypes['ACCEPT'], self.startscene_manager)
        self.register_button = gui_elements.createButton((500,450),'REGISTER',globals.buttonTypes['ACCEPT'], self.startscene_manager)
        self.exit_button = gui_elements.createButton((500,500),'EXIT',globals.buttonTypes['ACCEPT'], self.startscene_manager)
        

    def update(self, time_delta):
        self.startscene_manager.update(time_delta)

    def render(self, screen):
        self.startscene_manager.draw_ui(screen)
    
    def handleEvents(self, events):
        for event in events:
            self.startscene_manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.login_button:
                            print('login')
                            self.manager.goTo(Scenes.login_scene.LoginScene())
                        elif event.ui_element == self.register_button:
                            print('register')
                            self.manager.goTo(Scenes.registration_scene.RegistrationScene())
                        elif event.ui_element == self.guest_button:
                            print('guest')
                            globals.unsetUser()
                            self.manager.goTo(Scenes.mainmenue_scene.MainMenueScene())
                        elif event.ui_element == self.exit_button:
                            print('exit')
                            pygame.quit()
                            