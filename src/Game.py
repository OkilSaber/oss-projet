from hashlib import new
import pygame
import re
from constants.Assets import Assets
from constants.Colors import Colors
from constants.Context import Context
from elements.Button import Button
from elements.Rectangle import Rectangle
from elements.Text import Text
import Map
from json import load, dump
from typing import List, Tuple
import random

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
    map = []
    fruits = []
    direction = 'up'
    speed = 100
    snake = []
    head = tuple
    tail = tuple
    playing = bool
    gameover = False

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
                on_click=Button.new_game,
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
                on_click=Button.to_load,
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

    def create_loadable_maps_menu(self, map_list):
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

        y = 200
        for map in map_list:
            map_name_display = "Map: %s || Date: %s" % (map[0].upper(), map[1].strftime("%m/%d/%Y, %H:%M:%S"))
            self.buttons.append(
                Button(
                    on_click=Button.play_this_map,
                    rect=Rectangle(
                        position=(100, y),
                        color=(Colors.beige),
                        hover_color=(Colors.white),
                        size=(880, 100),
                    ),
                    text=Text(
                        text=map_name_display,
                        font="Corbel",
                        text_color=Colors.dark,
                        text_size=35,
                        text_position=(120, y + 30)
                    ),
                    metadata=map[0]
                )
            )

            self.buttons.append(
                Button(
                    on_click=Button.delete_map,
                    rect=Rectangle(
                        position=(990, y + 5),
                        color=(Colors.red),
                        hover_color=(Colors.light_red),
                        size=(110, 90),
                    ),
                    text=Text(
                        text="Delete",
                        font="Corbel",
                        text_color=Colors.white,
                        text_size=35,
                        text_position=(1000, y + 30)
                    ),
                    metadata=map[0]
                )
            )

            y+= 120

    def display_map(self):
        if self.map == None:
            return
        start_x = (1280-(17*40))/2
        start_y = ((720-(17*40))/2)
        self.rectangles.append(
            Rectangle(
                position=(start_x, start_y),
                color=(Colors.white),
                hover_color=None,
                size=(17*40, 17*40),
            )
        )

        y = start_y
        for row in self.map:
            x = start_x
            for block in row:
                if block in ["h", "s"]:
                    self.rectangles.append(
                        Rectangle(
                            position=(x, y),
                            size=(16, 16),
                            color=(Colors.red) if block == "h" else (Colors.dark),
                            hover_color=(Colors.red) if block == "h" else (Colors.dark),
                        )
                    )
                elif block == "f":
                    self.fruits.append((x, y))
                x += 17
            y += 17


    def check_buttons_click(self, position: Tuple[int, int]):
        for button in self.buttons:
            button.check_click(game=self, position=position)

    def draw_elements(self, position: Tuple[int, int]):
        for rect in self.rectangles:
            rect.draw(screen=self.screen, color=rect.color)
        for text in self.texts:
            text.draw(screen=self.screen)
        for fruit in self.fruits:
            self.screen.blit(pygame.transform.scale(pygame.image.load(Assets.apple_image),(17,17)), (fruit[0], fruit[1]))
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
        self.fruits = []
        self.create_options_menu_elements()

    def to_load(self):
        self.context = Context.LOAD_MAP
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.fruits = []
        map_list = Map.list_maps()
        self.create_loadable_maps_menu(map_list)

    def delete_map(self, map_name):
        Map.delete_map(map_name)
        self.to_load()

    def play_game_from_load(self, map_name):
        self.context = Context.IN_GAME
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.fruits = []
        self.map = Map.load_map(map_name)
        self.display_map()

    def spawn_fruit(self):
        x = round(random.randrange(0, Map.SIZE))
        y = round(random.randrange(0, Map.SIZE))
        if self.map[x][y] != '_':
            return self.spawn_fruit()
        self.map[x][y] = 'f'
        self.fruits = []
        self.fruits.append((x, y))

    def new_game(self):
        self.map = []
        for _ in range(Map.SIZE):
            self.map.append(list("_" * Map.SIZE))
        self.map[int(Map.SIZE/2)][int(Map.SIZE/2)] = "h"
        self.map[int(Map.SIZE/2)+1][int(Map.SIZE/2)] = "s"
        self.map[int(Map.SIZE/2)+2][int(Map.SIZE/2)] = "s"
        self.context = Context.IN_GAME
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.spawn_fruit()
        self.fruits = []
        self.display_map()
        self.head = tuple((int(Map.SIZE/2), int(Map.SIZE/2)))
        self.tail = tuple((int(Map.SIZE/2 + 2), int(Map.SIZE/2)))
        self.snake.append(self.head)
        self.snake.append(tuple((int(Map.SIZE/2 + 1), int(Map.SIZE/2))))
        self.snake.append(self.tail)
        self.playing = True

    def to_main_menu(self):
        self.context = Context.MAIN_MENU
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.fruits = []
        self.create_main_menu_buttons()

    def load_settings(self):
        try:
            self.settings = load(open("settings.json"))
        except Exception as e:
            settings = {
                "music": 0,
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

    def move_head(self, newhead):
        self.map[newhead[0]][newhead[1]] = 'h'
        self.map[self.head[0]][self.head[1]] = 's'
        self.head = newhead
        self.snake.insert(0, newhead)
        tail = self.snake.pop()
        self.map[tail[0]][tail[1]] = '_'

    def grow(self):
        last = self.snake[-1]
        blast = self.snake[-2]

        if blast[0] == last[0] and blast[1] == last[1] + 1 and last[1] - 1 > 0:
            tail = tuple((last[0], last[1] - 1))
        if blast[0] == last[0] and blast[1] == last[1] - 1 and last[1] + 1 < Map.SIZE:
            tail = tuple((last[0], last[1] + 1))
        if blast[1] == last[1] and blast[0] == last[0] + 1 and last[0] - 1 > 0:
            tail = tuple((last[0] - 1, last[1]))
        if blast[1] == last[1] and blast[0] == last[0] - 1 and last[0] + 1 < Map.SIZE:
            tail = tuple((last[0] + 1, last[1]))
        self.snake.append(tail)
        self.map[tail[0]][tail[1]] = '_'


    def move_up(self):
        newhead = tuple((self.head[0] - 1, self.head[1]))
        if newhead[0] < 0 or self.map[newhead[0]][newhead[1]] == 's':
            self.gameover = True
            return
        if self.map[newhead[0]][newhead[1]] == 'f':
            self.spawn_fruit()
            self.grow()
        self.move_head(newhead)

    def move_down(self):
        newhead = tuple((self.head[0] + 1, self.head[1]))
        if newhead[0] >= Map.SIZE or self.map[newhead[0]][newhead[1]] == 's':
            self.gameover = True
            return
        if self.map[newhead[0]][newhead[1]] == 'f':
            self.spawn_fruit()
            self.grow()
        self.move_head(newhead)

    def move_left(self):
        newhead = tuple((self.head[0], self.head[1] - 1))
        if newhead[1] < 0 or self.map[newhead[0]][newhead[1]] == 's':
            self.gameover = True
            return
        if self.map[newhead[0]][newhead[1]] == 'f':
            self.spawn_fruit()
            self.grow()
        self.move_head(newhead)

    def move_right(self):
        newhead = tuple((self.head[0], self.head[1] + 1))
        if newhead[1] >= Map.SIZE or self.map[newhead[0]][newhead[1]] == 's':
            self.gameover = True
            return
        if self.map[newhead[0]][newhead[1]] == 'f':
            self.spawn_fruit()
            self.grow()
            self.map[newhead[0]][newhead[1]] = '_'
        self.move_head(newhead)

    def move_snake(self):
        if self.direction == 'up' and self.playing:
            self.move_up()
        if self.direction == 'down':
            self.move_down()
        if self.direction == 'left':
            self.move_left()
        if self.direction == 'right':
            self.move_right()

    def change_direction(self, key):
        if key == pygame.K_LEFT and self.direction != 'right':
            self.direction = 'left'
        elif key == pygame.K_RIGHT and self.direction != 'left':
            self.direction = 'right'
        elif key == pygame.K_UP and self.direction != 'down':
            self.direction = 'up'
        elif key == pygame.K_DOWN and self.direction != 'up':
            self.direction = 'down'
