import pygame
import re
from elements.Rectangle import Rectangle
from elements.Text import Text
from typing import Tuple


class MapImage:
    def __init__(self, x, y, assetPath):
        self.x = x
        self.y = y
        self.assetPath = assetPath
        return

    def check_click(self, game, position: Tuple[int, int]):
        pass

    def draw(self, screen: pygame.Surface):
        screen.blit(pygame.transform.scale(pygame.image.load(self.assetPath),(17,17)), (self.x, self.y))
