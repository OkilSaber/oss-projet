import pygame
import re
from constants.Assets import Assets
from constants.Colors import Colors
from constants.Context import Context
from elements.Button import Button
from elements.Rectangle import Rectangle
from elements.Text import Text
from json import load, dump
from typing import List, Tuple


class Game:
    buttons: List[Button]
    texts: List[Text]
    rectangles: List[Rectangle]
    screen: pygame.Surface
    context: Context
    running: bool
    music_volume: float
    effects_volume: float
    settings: dict
    background_image_surface: pygame.Surface
    buttons = []
    texts = []
    rectangles = []

    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.context = Context.MAIN_MENU
        self.create_main_menu_buttons()
        self.running = True
        self.background_image_surface = pygame.image.load(
            Assets.menu_background_image
        )
        self.load_settings()
        pygame.mixer.init()
        pygame.mixer.music.load(Assets.background_music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.music_volume)

    def create_main_menu_buttons(self):
        self.buttons.append(
            Button(
                on_click=Button.click,
                rect=Rectangle(
                    position=(200, 44),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(880, 100),
                ),
                text=Text(
                    text="Play",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(640, 94)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.quit,
                rect=Rectangle(
                    position=(200, 188),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(880, 100),
                ),
                text=Text(
                    text="Load",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(640, 238)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.to_options,
                rect=Rectangle(
                    position=(200, 332),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(880, 100),
                ),
                text=Text(
                    text="Options",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(640, 382)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.click,
                rect=Rectangle(
                    position=(200, 476),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(880, 100),
                ),
                text=Text(
                    text="Ranking",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(640, 526)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.quit,
                rect=Rectangle(
                    position=(200, 620),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(880, 100),
                ),
                text=Text(
                    text="Exit",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(640, 670)
                ),
            )
        )

    def create_options_menu_elements(self):
        self.texts.append(
            Text(
                font="Corbel",
                text="Music Volume:",
                text_color=Colors.dark,
                text_position=(100, 200),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text=re.sub('[.,]', '', str(
                    round(pygame.mixer.music.get_volume(), 1) * 10)),
                text_color=Colors.dark,
                text_position=(500, 200),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Rebind controls",
                text_color=Colors.dark,
                text_position=(100, 300),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Up",
                text_color=Colors.dark,
                text_position=(125, 350),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Down",
                text_color=Colors.dark,
                text_position=(125, 400),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Left",
                text_color=Colors.dark,
                text_position=(125, 450),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Right",
                text_color=Colors.dark,
                text_position=(125, 500),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Pause",
                text_color=Colors.dark,
                text_position=(125, 550),
                text_size=35
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.to_main_menu,
                rect=Rectangle(
                    position=(20, 20),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(200, 100),
                ),
                text=Text(
                    text="Back",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(75, 50)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.volume_down,
                rect=Rectangle(
                    position=(300, 190),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(50, 50),
                ),
                text=Text(
                    text="-",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(315, 200)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.volume_up,
                rect=Rectangle(
                    position=(400, 190),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(50, 50),
                ),
                text=Text(
                    text="+",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(415, 200)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_up,
                rect=Rectangle(
                    position=(270, 345),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["up"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(305, 350)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_down,
                rect=Rectangle(
                    position=(270, 395),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["down"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(305, 400)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_left,
                rect=Rectangle(
                    position=(270, 445),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["left"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(305, 450)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_right,
                rect=Rectangle(
                    position=(270, 495),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["right"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(305, 500)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_pause,
                rect=Rectangle(
                    position=(270, 545),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["pause"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(305, 550)
                ),
            )
        )

    def check_buttons_click(self, position: Tuple[int, int]):
        for button in self.buttons:
            button.check_click(game=self, position=position)

    def draw_elements(self, position: Tuple[int, int]):
        for rect in self.rectangles:
            rect.draw(screen=self.screen, color=rect.color)
        for text in self.texts:
            text.draw(screen=self.screen)
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
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()

    def to_main_menu(self):
        self.context = Context.MAIN_MENU
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_main_menu_buttons()

    def load_settings(self):
        try:
            self.settings = load(open("settings.json"))
        except Exception as e:
            settings = {
                "music": 100,
                "effects": 100,
                "up": "up",
                "down": "down",
                "left": "left",
                "right": "right"
            }
            settings_file = open('settings.json', 'w')
            dump(settings, settings_file)
            self.settings = settings
        self.music_volume = self.settings["music"] / 100
        self.effects_volume = self.settings["effects"] / 100

    def update_settings(self, key, value):
        self.settings[key] = value
        dump(self.settings, open('settings.json', 'w'))

    def change_binding_up(self, key):
        self.update_settings("up", key)
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_down(self, key):
        self.update_settings("down", key)
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_left(self, key):
        self.update_settings("left", key)
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_right(self, key):
        self.update_settings("right", key)
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_pause(self, key):
        self.update_settings("pause", key)
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return
