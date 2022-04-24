from typing import Tuple
import pygame

from Context import Context


class Button:
    def __init__(
        self,
        position: Tuple[int, int],
        size: Tuple[int, int],
        color: Tuple[int, int, int],
        hover_color: Tuple[int, int, int],
        text_color: Tuple[int, int, int],
        text: str,
        font: str,
        text_size: int,
        text_position: Tuple[int, int],
        on_click,
    ):
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.text = text
        self.on_click = on_click
        self.font = font
        self.text_size = text_size
        self.pygame_font = pygame.font.SysFont(font, text_size)
        self.pygame_text = self.pygame_font.render(
            self.text,
            True,
            self.text_color
        )
        self.text_position = text_position
        return

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(
            screen,
            self.color,
            [
                self.position[0],
                self.position[1],
                self.size[0],
                self.size[1]
            ],
        )
        screen.blit(self.pygame_text, self.text_position)

    def on_hover(self, mouse: Tuple[int, int], screen: pygame.Surface):
        if mouse[0] > self.position[0] \
                and mouse[0] < (self.position[0] + self.size[0]) \
                and mouse[1] > self.position[1] \
                and mouse[1] < (self.position[1] + self.size[1]):
            pygame.draw.rect(
                screen,
                self.hover_color,
                [
                    self.position[0],
                    self.position[1],
                    self.size[0],
                    self.size[1]
                ],
            )
        else:
            pygame.draw.rect(
                screen,
                self.color,
                [
                    self.position[0],
                    self.position[1],
                    self.size[0],
                    self.size[1]
                ],
            )
        screen.blit(self.pygame_text, self.text_position)

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
