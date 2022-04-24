from Game import Game
import pygame

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
    for button in game.buttons:
        button.draw(screen=game.screen)
    game.check_buttons_hover(position=pygame.mouse.get_pos())
    pygame.display.update()
