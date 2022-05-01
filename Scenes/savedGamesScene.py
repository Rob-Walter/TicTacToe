import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
import Scenes.game_Scene
from database_controller import DB_Controller

class SavedGamesScene(Scene):
    #GUI Manager
    def __init__(self):

        self.ButtonListWithGameNumber = []
        self.savedGames_manager = pygame_gui.UIManager((1200, 800), 'theme.json')
        self.savedGames = self.loadSavedGames()
        self.createSaveGameEntry(self.savedGames)
        self.back_button = gui_elements.createButton((0,400),'BACK','ACCEPT', self.savedGames_manager)

    def createSaveGameEntry(self, data):
        if len(data) > 0:
            for entryIndex, entry in enumerate(data):
                print(data)
                positionY = entryIndex * 60
                dateTextBox =gui_elements.createTextfeld((0,positionY), entry[3], globals.textboxTypes['SAVE'],self.savedGames_manager)
                loadEntryButton = gui_elements.createButton((260,positionY),"Spielstand laden",globals.buttonTypes["ACCEPT"],self.savedGames_manager)
                self.ButtonListWithGameNumber.append((loadEntryButton, entry[0]))
        else:
            textBox = gui_elements.createTextfeld((0,0), "Keine Spielstände vorhanden", globals.textboxTypes['SAVE'],self.savedGames_manager)


    def loadSavedGames(self):
        dbcontroller = DB_Controller()
        return dbcontroller.loadSavedGames()

    def loadSaveGameAndInitiliaseGame(self,gameNumber):
        dbcontroller = DB_Controller()
        result = dbcontroller.loadSaveFileGame(globals.user["id"],gameNumber)
        ki_strength = result[0][6]
        self.manager.goTo(Scenes.game_Scene.GameScene(True,ki_strength,result))

    def update(self, time_delta):
        self.savedGames_manager.update(time_delta)

    def render(self, screen):
        self.savedGames_manager.draw_ui(screen)

    def handleEvents(self, events):
        for event in events:
            self.savedGames_manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        for entry in self.ButtonListWithGameNumber:
                            print("Entry: ",entry)
                            if event.ui_element == entry[0]:
                                print(entry[1])
                                self.loadSaveGameAndInitiliaseGame(entry[1])
                        if event.ui_element == self.back_button:
                            print('back')
                            self.manager.goTo(Scenes.mainmenue_scene.MainMenueScene())
                                
                     
