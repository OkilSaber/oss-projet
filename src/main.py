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
            if game.gameover and not (len(game.snakes) == 1 and game.snakes[0].is_bot):
                game.player_name(event)
            if game.context == Context.IN_GAME:
                for snake in game.snakes:
                    if not snake.is_bot:
                        snake.change_direction_keyboard(event.key)
                if event.key == pygame.key.key_code(game.settings["first_player_controls"]['pause']):
                    game.to_pause_menu(False)
            if game.context == Context.DUAL_GAME:
                for snake in game.snakes:
                    snake.change_direction_keyboard(event.key)
                if event.key == pygame.key.key_code(game.settings["first_player_controls"]['pause']):
                    game.to_pause_menu(True)
                elif event.key == pygame.key.key_code(game.settings["second_player_controls"]['pause']):
                    game.to_pause_menu(True)
        game.check_key_binding_input(event)
    if game.gameover == True:
        is_bot = len(game.snakes) == 1 and game.snakes[0].is_bot
        if game.context == Context.DUAL_GAME:
            game.to_main_menu()
        else:
            game.loose(is_bot)
        game.playing = False
    elif game.playing == True and game.gameover == False and pygame.time.get_ticks() - ticks > game.speed:
        ticks = pygame.time.get_ticks()
        game.map_images.clear()
        (alive, loser_id) = game.move_snakes()
        if not alive:
            game.gameover = True
            if len(game.snakes) == 2:
                # if there is 2 player, the final score is the score of the not losing player
                game.final_score = game.snakes[(loser_id + 1) % 2].score
            else:
                game.final_score = game.snakes[0].score
        game.display_map()
    game.draw_elements(position=pygame.mouse.get_pos())
    pygame.display.update()
