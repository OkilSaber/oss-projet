import pygame
from Game import Game

pygame.init()
game = Game()
bg = pygame.image.load("assets/menu_background.png")
while game.running:
    game.screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            game.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print(mouse)
            game.check_buttons_click(mouse)
    for button in game.buttons:
        button.draw(screen=game.screen)
    pygame.display.update()
