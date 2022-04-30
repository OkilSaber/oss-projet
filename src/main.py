from operator import truediv
from shutil import move
from Game import Game
import pygame
from constants.Context import Context

pygame.init()
game = Game()
ticks = pygame.time.get_ticks()
while game.running:
    game.screen.blit(game.background_image_surface, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            game.check_buttons_click(mouse)
        if event.type == pygame.KEYDOWN:
            game.change_direction(event.key)
        game.check_key_binding_input(event)
    if game.playing == True and pygame.time.get_ticks() - ticks > game.speed:
        game.move_snake()
        ticks = pygame.time.get_ticks()
        game.display_map()
    if game.gameover:
        game.playing = False
    game.draw_elements(position=pygame.mouse.get_pos())
    pygame.display.update()
