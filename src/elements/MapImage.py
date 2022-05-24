import pygame
from typing import Tuple
from constants.Screen import Screen

class MapImage:
    def __init__(self, x, y, assetPath):
        self.x = x
        self.y = y
        self.assetPath = assetPath
        return

    def check_click(self, game, position: Tuple[int, int]):
        pass

    def draw(self, screen: pygame.Surface):
        screen.blit(
            pygame.transform.scale(
                pygame.image.load(self.assetPath),
                (Screen.SQUARE_SIZE, Screen.SQUARE_SIZE)
            ),
            (self.x, self.y)
        )
