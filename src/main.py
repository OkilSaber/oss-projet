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
            if game.gameover:
                game.player_name(event)
            if game.context == Context.IN_GAME:
                for snake in game.snakes:
                    if not snake.is_bot:
                        snake.change_direction_keyboard(event.key)  
                if event.key == pygame.key.key_code(game.settings['pause']):
                    game.to_pause_menu()
        game.check_key_binding_input(event)
    if game.gameover == True:
        game.loose(event)
        game.playing = False
    elif game.playing == True and game.gameover == False and pygame.time.get_ticks() - ticks > game.speed:
        ticks = pygame.time.get_ticks()
        game.map_images.clear()
        (alive, loser_id) = game.move_snakes()
        if not alive:
            game.gameover = True
            if len(game.snakes) == 2:
                game.final_score = game.snakes[(loser_id + 1) % 2].score # if there is 2 player, the final score is the score of the not losing player
            else:
                game.final_score = game.snakes[0].score
        game.display_map()
    game.draw_elements(position=pygame.mouse.get_pos())
    pygame.display.update()
