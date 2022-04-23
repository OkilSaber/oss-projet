import pygame
import sys
import colors

pygame.init()
res = (1280, 720)
screen = pygame.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('quit', True, colors.white)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
    screen.fill((60, 25, 60))
    mouse = pygame.mouse.get_pos()
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen, colors.light, [width/2, height/2, 140, 40])
    else:
        pygame.draw.rect(screen, colors.dark, [width/2, height/2, 140, 40])
    screen.blit(text, (width/2+50, height/2))
    pygame.display.update()
