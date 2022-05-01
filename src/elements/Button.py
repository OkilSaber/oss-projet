import pygame
import re
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
        game.delete_map(self.metadata)

    def play_this_save(self, game):
        game.play_sound("assets/button_click.mp3")
        game.play_game_from_load(self.metadata)

    def new_game(self, game):
        game.play_sound("assets/button_click.mp3")
        game.new_game()

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
