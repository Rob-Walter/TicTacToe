import pygame
import pygame.freetype
import pygame_gui
import Scenes.mainmenue_scene
import globals
import gui_elements
from board import Board
from player import Player
from database_controller import DB_Controller
import customEvents
from Scenes.scene import Scene
import minmax

pygame.freetype.init()

class GameScene(Scene):
    
    def __init__(self, isLoaded, ki_strength, loadData = None) -> None:
        super().__init__()
        if not isLoaded:
            globals.unsetGameNumber()
    
        self.BOARD_WIDTH, self.BOARD_HEIGHT = 600, 600

        globals.setStartingPoints((globals.screenWidth - self.BOARD_WIDTH) / 2, (globals.screenHeight - self.BOARD_HEIGHT) / 2)

        self.board = Board( self.BOARD_WIDTH, self.BOARD_HEIGHT, isLoaded, loadData)

        self.playerWhite = Player("white")
        self.playerBlack = Player("black")
        self.playerWhiteMovable = True
        self.playerBlackMovable = True
        self.ki_strength = ki_strength
        if ki_strength == 'EASY':
            self.ki = 1
        elif ki_strength == 'MEDIUM':
            self.ki = 2
        elif ki_strength == 'HARD':
            self.ki = 3
        self.currentTurnPlayer = self.playerWhite

        #GUI Manager
        self.game_manager = pygame_gui.UIManager((1200, 800), 'theme.json')
        if globals.user != None:
            self.save_game_button = gui_elements.createButton((0,300),'SAVE',globals.buttonTypes['ACCEPT'], self.game_manager)
        self.back_game_button = gui_elements.createButton((0,350),'BACK',globals.buttonTypes['ACCEPT'], self.game_manager)
        self.rules_game_button = gui_elements.createButton((0,400),'RULES',globals.buttonTypes['ACCEPT'], self.game_manager)
        self.exit_game_button = gui_elements.createButton((0,450),'EXIT',globals.buttonTypes['ACCEPT'], self.game_manager)
        self.rules_label = gui_elements.createTextfeld((200,150),"Bauernschach ist eine Variante des Schachs nur mit Bauern und auf einem <br>6x6 Feld. Schwarze sowie weiße Figuren stehen dabei an der <br>gegenüberliegenden Grundlinie. Die Farbe weiß beginnt den Zug, danach folgen die <br>schwarzen Figuren. Zwei Züge sind erlaubt: Ein Bauer darf nach vorne <br>ziehen wenn das vordere Feld frei ist. Es muss dabei in die Richtung <br>der gegnerischen Grundlinie bewegen. Schlagen darf der Bauer in Richtung der <br>gegnerischen Grundlinie durch diagonales Ziehen in Richtung der gegnerischen Grundlinie, <br>aber auch nur wenn auf diesem Feld ein gegnerischer Bauer steht. <br>Der “geschlagene” Bauer wird vom Spielbrett genommen. Gewonnen hat man das <br>Spiel wenn man einen eigenen Bauern auf die gegnerische Grundlinie platziert. <br>Die Farbe die dies erreicht, ist der Sieger. Wenn ein Spieler weder Züge oder Figuren <br>hat zählt das Spiel für ihn verloren. In dieser Variante des <br>Bauernschachs gibt es kein Unentschieden.",globals.textboxTypes['RULES'], self.game_manager)
        self.rules_label.visible=0
        self.strength_label = gui_elements.createTextfeld((0,150),self.ki_strength,globals.textboxTypes['INFO'], self.game_manager)


    def switchCurrentTurnPlayer(self):
        if self.currentTurnPlayer == self.playerBlack:
            self.currentTurnPlayer = self.playerWhite

        elif self.currentTurnPlayer == self.playerWhite:
            self.currentTurnPlayer = self.playerBlack
            result = minmax.minimax(self.board,None, 2, True,float("-inf"), float("+inf"),)
            print("RESULT: ", result)
            self.board.move(result[2],"black")
            self.board.checkForWinOrDraw()
            self.switchCurrentTurnPlayer()    

    
    def render(self, screen):
        screen.blit(self.board.draw(),(globals.boardStartingPointX, globals.boardStartingPointY))
        self.game_manager.draw_ui(screen)

    def update(self, timeDelta):
        self.game_manager.update(timeDelta) 

    def savegame(self):
        dbcontroller = DB_Controller()
        dbcontroller.savefilegame(globals.user['id'],self.board, self.currentTurnPlayer.getTeam(), self.ki_strength)

    def insertintoleaderboard(self, win, loss):
        if globals.user != None:
            dbcontroller = DB_Controller()
            dbcontroller.insertgameintoleaderboard(self.ki_strength, win, loss)
        else:
            return

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                    self.board.moveMouse(event, self.currentTurnPlayer)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.board.mousePressed(event, self.currentTurnPlayer)
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     self.board.mouseReleased(event, self.currentTurnPlayer)
            elif event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.back_game_button:
                            print('back')
                            self.manager.goTo(Scenes.mainmenue_scene.MainMenueScene())
                        elif event.ui_element == self.rules_game_button:
                            if self.rules_label.visible == 0:
                                print('rules on')
                                self.rules_label.visible = 1
                            elif self.rules_label.visible == 1:
                                print('rules off')
                                self.rules_label.visible = 0
                        elif event.ui_element == self.exit_game_button:
                            print('exit')
                            pygame.quit()
                        elif event.ui_element == self.save_game_button:
                            print('save game')
                            self.savegame()
                if hasattr(event, 'customType'):
                    if event.customType == customEvents.PLAYERWIN:
                        if event.winner == "white":
                            print("Weiß gewinnt")
                            self.insertintoleaderboard(1, 0)
                            self.manager.goTo(Scenes.mainmenue_scene.MainMenueScene())
                        if event.winner == "black":
                            print("Black gewinnt")
                            self.insertintoleaderboard(0, 1)
                            self.manager.goTo(Scenes.mainmenue_scene.MainMenueScene())
                    elif event.customType == customEvents.DRAW:
                        print("Unentschieden")
                        self.manager.goTo(Scenes.mainmenue_scene.MainMenueScene())
                    elif event.customType == customEvents.PLAYERMOVED:
                        self.switchCurrentTurnPlayer()
            self.game_manager.process_events(event)

