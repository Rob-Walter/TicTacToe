import pygame
import pygame.freetype
from Scenes.game_Scene import GameScene
import globals
from sceneManager import SceneManager

pygame.init()
WIDTH, HEIGHT = 1200,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
globals.setScreenDimensions(WIDTH,HEIGHT)
pygame.display.set_caption("TIC TAC TOE")
FPS = 60
ORANGE = (235, 180, 52)
sceneManager = SceneManager()

def draw_window():
    WIN.fill((32,140,122))


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        time_delta = clock.tick(FPS)/1000.0
        if pygame.event.get(pygame.QUIT):
            run = False
            break

        sceneManager.scene.handleEvents(pygame.event.get())
        sceneManager.scene.update(time_delta)
        draw_window()
        sceneManager.scene.render(WIN)
        pygame.display.update()
       

        

    pygame.quit()

if __name__ == "__main__":
    main() 