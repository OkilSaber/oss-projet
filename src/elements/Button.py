import pygame
import re
import Saves
from elements.Rectangle import Rectangle
from elements.Text import Text
from typing import Tuple
from constants.Context import Context


class Button:
    rect: Rectangle
    text: Text

    def __init__(
        self,
        rect: Rectangle,
        text: Text,
        on_click,
        metadata=None,
    ):
        self.rect = rect
        self.text = text
        self.on_click = on_click
        self.metadata = metadata
        return

    def check_click(self, game, position: Tuple[int, int]):
        if (self.rect.rectObject.collidepoint(position)):
            self.on_click(self=self, game=game)

    def draw(self, screen: pygame.Surface, color: Tuple[int, int, int]):
        self.rect.draw(screen=screen, color=color)
        self.text.draw(screen=screen)

    def on_hover(self, mouse: Tuple[int, int], screen: pygame.Surface):
        try:
            if(self.rect.rectObject.collidepoint(mouse)):
                self.draw(screen=screen, color=self.rect.hover_color)
            else:
                self.draw(screen=screen, color=self.rect.color)
        except Exception as e:
            print(e)

    def quit(self, game):
        game.play_sound("assets/button_click.mp3")
        game.running = False

    def to_options(self, game):
        game.play_sound("assets/button_click.mp3")
        game.to_options()

    def to_load(self, game):
        game.play_sound("assets/button_click.mp3")
        game.to_load()

    def to_main_menu(self, game):
        game.play_sound("assets/button_click.mp3")
        game.to_main_menu()

    def delete_save(self, game):
        game.play_sound("assets/button_click.mp3")
        game.delete_save(self.metadata)

    def play_this_save(self, game):
        game.play_sound("assets/button_click.mp3")
        game.play_game_from_load(self.metadata)

    def new_game(self, game):
        game.play_sound("assets/button_click.mp3")
        game.new_game()

    def new_game_autoplayer(self, game):
        game.play_sound("assets/button_click.mp3")
        game.new_game_autoplayer()

    def new_dual_game(self, game):
        game.play_sound("assets/button_click.mp3")
        game.new_dual_game()

    def save_rank(self, game):
        game.play_sound("assets/button_click.mp3")
        game.save_rank()

    def to_ranking(self, game):
        game.play_sound("assets/button_click.mp3")
        game.to_ranking()

    def volume_up(self, game):
        current_volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(current_volume + 0.1)
        current_volume = round(pygame.mixer.music.get_volume(), 1)
        game.update_settings("music", current_volume * 100)
        game.texts[1].text = re.sub('[.,]', '', str(current_volume * 10))
        game.texts[1].pygame_text = game.texts[1].pygame_font.render(
            game.texts[1].text,
            True,
            game.texts[1].text_color
        )

    def volume_down(self, game):
        current_volume = pygame.mixer.music.get_volume()
        if (current_volume - 0.1 < 0):
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(current_volume - 0.1)
        current_volume = round(pygame.mixer.music.get_volume(), 1)
        game.update_settings("music", current_volume * 100)
        game.texts[1].text = re.sub('[.,]', '', str(current_volume * 10))
        game.texts[1].pygame_text = game.texts[1].pygame_font.render(
            game.texts[1].text,
            True,
            game.texts[1].text_color
        )

    def change_context_up_second(self, game):
        game.context = Context.OPTIONS_WAITING_INPUT_UP_SECOND

    def change_context_down_second(self, game):
        game.context = Context.OPTIONS_WAITING_INPUT_DOWN_SECOND

    def change_context_left_second(self, game):
        game.context = Context.OPTIONS_WAITING_INPUT_LEFT_SECOND

    def change_context_right_second(self, game):
        game.context = Context.OPTIONS_WAITING_INPUT_RIGHT_SECOND

    def change_context_pause_second(self, game):
        game.context = Context.OPTIONS_WAITING_INPUT_PAUSE_SECOND

    def change_context_up(self, game):
        game.context = Context.OPTIONS_WAITING_INPUT_UP

    def change_context_down(self, game):
        game.context = Context.OPTIONS_WAITING_INPUT_DOWN

    def change_context_left(self, game):
        game.context = Context.OPTIONS_WAITING_INPUT_LEFT

    def change_context_right(self, game):
        game.context = Context.OPTIONS_WAITING_INPUT_RIGHT

    def change_context_pause(self, game):
        game.context = Context.OPTIONS_WAITING_INPUT_PAUSE

    def click(self, game):
        game.play_sound("assets/button_click.mp3")

    def pause_resume_game(self, game):
        game.buttons.clear()
        game.rectangles.clear()
        game.texts.clear()
        game.map_images.clear()
        game.playing = True
        game.context = Context.IN_GAME

    def pause_save_game(self, game):
        Saves.save(
            game.save_count, game.snakes[0].snake, game.fruits[0].pos, game.snakes[0].direction)
        game.save_count += 1
        game.to_main_menu()

    def pause_restart_game(self, game):
        game.buttons.clear()
        game.rectangles.clear()
        game.texts.clear()
        game.map_images.clear()
        game.snakes.clear()
        game.new_game()

    def pause_dual_restart_game(self, game):
        game.buttons.clear()
        game.rectangles.clear()
        game.texts.clear()
        game.map_images.clear()
        game.snakes.clear()
        game.fruits.clear()
        game.new_dual_game()

    def pause_quit_game(self, game):
        game.to_main_menu()
