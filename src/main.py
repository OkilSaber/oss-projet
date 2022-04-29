from Game import Game
import pygame
from constants.Context import Context

pygame.init()
game = Game()
while game.running:
    game.screen.blit(game.background_image_surface, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            game.check_buttons_click(mouse)
        if event.type == pygame.KEYDOWN:
            if game.context == Context.OPTIONS_WAITING_INPUT_UP:
                game.change_binding_up(pygame.key.name(event.key))
            elif game.context == Context.OPTIONS_WAITING_INPUT_DOWN:
                game.change_binding_down(pygame.key.name(event.key))
            elif game.context == Context.OPTIONS_WAITING_INPUT_LEFT:
                game.change_binding_left(pygame.key.name(event.key))
            elif game.context == Context.OPTIONS_WAITING_INPUT_RIGHT:
                game.change_binding_right(pygame.key.name(event.key))
            elif game.context == Context.OPTIONS_WAITING_INPUT_PAUSE:
                game.change_binding_pause(pygame.key.name(event.key))
    game.draw_elements(position=pygame.mouse.get_pos())
    pygame.display.update()
