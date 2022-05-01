from operator import truediv
from shutil import move
from Game import Game
import pygame
from constants.Context import Context

pygame.init()
game = Game()
ticks = pygame.time.get_ticks()
clock = pygame.time.Clock()
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
            if game.gameover:
                game.player_name(event)
        game.check_key_binding_input(event)
    if game.gameover == True:
        game.loose(event)
        game.playing = False
    elif game.playing == True and game.gameover == False and pygame.time.get_ticks() - ticks > game.speed:
        ticks = pygame.time.get_ticks()
        game.map_images.clear()
        game.move_snake()
        game.display_map()
    game.draw_elements(position=pygame.mouse.get_pos())
    pygame.display.update()
