from typing import Tuple
import pygame

from Rectangle import Rectangle
from Text import Text


class Button:
    rect: Rectangle
    text: Text

    def __init__(
        self,
        rect: Rectangle,
        text: Text,
        on_click,
    ):
        self.rect = rect
        self.text = text
        self.on_click = on_click
        return

    def check_click(self, game, position: Tuple[int, int]):
        if position[0] > self.rect.position[0] \
                and position[0] < (self.rect.position[0] + self.rect.size[0]) \
                and position[1] > self.rect.position[1] \
                and position[1] < (self.rect.position[1] + self.rect.size[1]):
            self.on_click(self=self, game=game)

    def draw(self, screen: pygame.Surface):
        self.rect.draw(screen=screen, )
        self.text.draw(screen=screen)

    def on_hover(self, mouse: Tuple[int, int], screen: pygame.Surface):
        if mouse[0] > self.rect.position[0] \
                and mouse[0] < (self.rect.position[0] + self.rect.size[0]) \
                and mouse[1] > self.rect.position[1] \
                and mouse[1] < (self.rect.position[1] + self.rect.size[1]):
            self.rect.draw(screen=screen, color=self.rect.hover_color)
        else:
            self.rect.draw(screen=screen, color=self.rect.color)
        self.text.draw(screen=screen)

    def quit(self, game):
        game.play_sound("assets/button_click.mp3")
        game.running = False

    def to_options(self, game):
        game.play_sound("assets/button_click.mp3")
        game.to_options()

    def to_main_menu(self, game):
        game.play_sound("assets/button_click.mp3")
        game.to_main_menu()

    def click(self, game):
        game.play_sound("assets/button_click.mp3")
