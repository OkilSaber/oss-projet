import pygame
from typing import Tuple


class Rectangle:
    position: Tuple[int, int]
    size: Tuple[int, int]
    color: Tuple[int, int, int]
    hover_color: Tuple[int, int, int]

    def __init__(
        self,
        position: Tuple[int, int],
        size: Tuple[int, int],
        color: Tuple[int, int, int],
        hover_color: Tuple[int, int, int],
    ):
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = hover_color
        return

    def draw(self, screen: pygame.Surface, color: Tuple[int, int, int]):
        pygame.draw.rect(
            screen,
            color,
            [
                self.position[0],
                self.position[1],
                self.size[0],
                self.size[1]
            ],
        )
