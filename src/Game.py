from typing import List, Tuple

import pygame
import colors
from Button import Button


class Game:
    MAIN_MENU = 1
    IN_GAME = 2
    PAUSE = 3
    OPTIONS = 4
    buttons: List[Button]
    buttons = []
    running = True

    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.context = Game.MAIN_MENU
        self.create_buttons()

    def create_buttons(self):
        self.buttons.append(
            Button(
                position=(200, 150),
                color=(colors.beige),
                hover_color=(colors.white),
                on_click=click,
                size=(880, 100),
                text="Play",
                font="Corbel",
                text_color=colors.dark,
                text_size=35,
                text_position=(640, 175)
            )
        )
        self.buttons.append(
            Button(
                position=(200, 300),
                color=(colors.beige),
                hover_color=(colors.white),
                on_click=click,
                size=(880, 100),
                text="Load",
                font="Corbel",
                text_color=colors.dark,
                text_size=35,
                text_position=(640, 325)
            )
        )
        self.buttons.append(
            Button(
                position=(200, 450),
                color=(colors.beige),
                hover_color=(colors.white),
                on_click=click,
                size=(880, 100),
                text="Options",
                font="Corbel",
                text_color=colors.dark,
                text_size=35,
                text_position=(640, 475)
            )
        )
        self.buttons.append(
            Button(
                position=(200, 600),
                color=(colors.beige),
                hover_color=(colors.white),
                on_click=Button.quit,
                size=(880, 100),
                text="Quit",
                font="Corbel",
                text_color=colors.dark,
                text_size=35,
                text_position=(640, 625)
            )
        )

    def check_buttons_click(self, position: Tuple[int, int]):
        for button in self.buttons:
            if position[0] > button.position[0] \
                    and position[0] < (button.position[0] + button.size[0]) \
                    and position[1] > button.position[1] \
                    and position[1] < (button.position[1] + button.size[1]):
                button.on_click(self=button, game=self)

    def check_buttons_hover(self,
                            position: Tuple[int, int],):
        for button in self.buttons:
            button.on_hover(mouse=position, screen=self.screen)


def click():
    print("click")
