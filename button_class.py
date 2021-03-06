import pygame
import pygame_gui

def draw():        
    pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.x, self.y), (self.height, self.width)),text=self.text,manager=self.manager)

pygame.init()

pygame.display.set_caption('')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#030000'))
exit_manager = pygame_gui.UIManager((800, 600), 'exit.json')
exit_button = Button(350, 275, 100, 50, 'Exit', exit_manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == exit_button:
                    print('Exit')

        exit_manager.process_events(event)

    exit_manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    exit_manager.draw_ui(window_surface)

    pygame.display.update()