from operator import truediv
from shutil import move
from Game import Game
import pygame

pygame.init()
game = Game()
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
            game.change_direction(event.type)
    if game.playing == True:
        game.move_snake()
        game.display_map()
    if game.gameover:
        game.playing = False
    clock.tick(2000)
    game.draw_elements(position=pygame.mouse.get_pos())
    pygame.display.update()
