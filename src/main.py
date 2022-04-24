import pygame
import Game


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('assets/background_music.ogg')
pygame.mixer.music.play(-1)
game = Game()
bg = pygame.image.load("assets/menu_background.png")
while game.running:
    game.screen.blit(bg, (0, 0))
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
