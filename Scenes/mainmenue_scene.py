import Scenes.leaderboard_scene
from Scenes.savedGamesScene import SavedGamesScene
import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
import Scenes.game_Scene
import Scenes.start_scene
from database_controller import DB_Controller

class MainMenueScene(Scene):
    #GUI Manager
    def __init__(self):
        self.username = ""
        self.password = ""
        self.count = 0
        self.starting_y = 300
        self.starting_x = 0

        self.mainmenue_manager = pygame_gui.UIManager((1200, 800), 'theme.json')

        self.new_game_button = gui_elements.createButton((0,self.starting_y + self.count*50),'NEW GAME',globals.buttonTypes['ACCEPT'], self.mainmenue_manager)
        #print(self.new_game_button.get_relative_rect().width)
        self.ki_strength_option = gui_elements.createdropwdown((140,self.starting_y + self.count*50),['EASY','MEDIUM','HARD'],"EASY", self.mainmenue_manager)
        self.count += 1
        if globals.user != None:
            self.load_game_button = gui_elements.createButton((0,self.starting_y + self.count*50),'LOAD GAME',globals.buttonTypes['ACCEPT'], self.mainmenue_manager)
            self.count += 1
            self.leaderboard_button = gui_elements.createButton((0,self.starting_y + self.count*50),'LEADERBOARD',globals.buttonTypes['ACCEPT'], self.mainmenue_manager)
            self.count += 1
        self.back_button = gui_elements.createButton((0,self.starting_y + self.count*50),'BACK',globals.buttonTypes['ACCEPT'], self.mainmenue_manager)
        self.count += 1
        self.exit_button = gui_elements.createButton((0,self.starting_y + self.count*50),'EXIT',globals.buttonTypes['ACCEPT'], self.mainmenue_manager)

    def login(self):
        dbcontroller = DB_Controller()
        return dbcontroller.checkifplayerexistinDB(self.username, self.password)

    def loadSavedGames(self):
        dbcontroller = DB_Controller()
        print(dbcontroller.loadSavedGames(globals.user["id"]))

    def update(self, time_delta):
        self.mainmenue_manager.update(time_delta)

    def render(self, screen):
        self.mainmenue_manager.draw_ui(screen)

    def handleEvents(self, events):
        for event in events:
            self.mainmenue_manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.back_button:
                            print('start scene')
                            self.manager.goTo(Scenes.start_scene.StartScene())
                        elif event.ui_element == self.exit_button:
                            print('exit')
                            pygame.quit()
                        elif event.ui_element == self.new_game_button:
                            print('new game')
                            ki_strength = self.ki_strength_option.selected_option
                            print("KI STRENGTH: ",ki_strength)
                            self.manager.goTo(Scenes.game_Scene.GameScene(False, ki_strength))
                        elif globals.user != None:
                            if event.ui_element == self.load_game_button:
                                self.manager.goTo(SavedGamesScene())
                            elif event.ui_element == self.leaderboard_button:
                                print('leaderboard')
                                self.manager.goTo(Scenes.leaderboard_scene.LeaderboardScene())