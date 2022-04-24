import json
from Button import Button
from Context import Context
from typing import List, Tuple
import constants.assets as assets
import constants.colors as colors
import pygame


class Game:
    buttons: List[Button]
    screen: pygame.Surface
    context: Context
    running: bool
    music_volume: float
    effects_volume: float
    settings: dict
    background_image_surface: pygame.Surface
    buttons = []

    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.context = Context.MAIN_MENU
        self.create_main_menu_buttons()
        self.running = True
        self.background_image_surface = pygame.image.load(
            assets.menu_background_image
        )
        self.load_settings()
        pygame.mixer.init()
        pygame.mixer.music.load(assets.background_music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.music_volume)

    def create_main_menu_buttons(self):
        self.buttons.append(
            Button(
                position=(200, 150),
                color=(colors.beige),
                hover_color=(colors.white),
                on_click=Button.click,
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
                on_click=Button.quit,
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
                on_click=Button.to_options,
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

    def change_background_image(self, background_image: str):
        self.background_image_surface = pygame.image.load(background_image)

    def change_background_music(self, background_music: str):
        pygame.mixer.stop()
        pygame.mixer.music.load(background_music)
        pygame.mixer.music.play(-1)

    def play_sound(self, sound: str):
        sound = pygame.mixer.Sound(sound)
        sound.play()

    def to_options(self):
        self.context = Context.OPTIONS
        self.buttons.clear()

    def load_settings(self):
        self.settings = json.load(open("settings.json"))
        self.music_volume = self.settings["music"] / 100
        self.effects_volume = self.settings["effects"] / 100
