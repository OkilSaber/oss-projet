import pygame


class Button:
    def __init__(self,
                 position: tuple[int, int],
                 size: tuple[int, int],
                 color: tuple[int, int, int],
                 text: str,
                 on_click,
                 ):
        self.position = position
        self.size = size
        self.color = color
        self.text = text
        self.on_click = on_click
        return

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen,
                         self.color,
                         [
                             self.position[0],
                             self.position[1],
                             self.size[0],
                             self.size[1]
                         ],
                         )
