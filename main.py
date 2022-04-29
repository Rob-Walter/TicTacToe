import pygame
import pygame.freetype
import globals
from sceneManager import SceneManager

WIDTH, HEIGHT = 1200,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
globals.setScreenDimensions(WIDTH,HEIGHT)
pygame.display.set_caption("Bauernschach")
FPS = 60
ORANGE = (235, 180, 52)
sceneManager = SceneManager()

def draw_window():
    WIN.fill(ORANGE)


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        time_delta = clock.tick(FPS)/1000.0
        if pygame.event.get(pygame.QUIT):
            run = False
            return

        sceneManager.scene.handleEvents(pygame.event.get())
        sceneManager.scene.update(time_delta)
        draw_window()
        sceneManager.scene.render(WIN)
        pygame.display.update()
       

        

    pygame.quit()

if __name__ == "__main__":
    main() 