import pygame
from typing import Tuple


class Text:
    text_color: Tuple[int, int, int]
    text: str
    font: str
    text_size: int
    text_position: Tuple[int, int]

    def __init__(
        self,
        text_color: Tuple[int, int, int],
        text: str,
        font: str,
        text_size: int,
        text_position: Tuple[int, int],
    ):
        self.text_color = text_color
        self.text = text
        self.font = font
        self.text_size = text_size
        self.pygame_font = pygame.font.SysFont(font, text_size)
        print(self.text_color[0])
        self.pygame_text = self.pygame_font.render(
            self.text,
            True,
            self.text_color
        )
        self.text_position = text_position
        return

    def draw(self, screen: pygame.Surface):
        screen.blit(self.pygame_text, self.text_position)
