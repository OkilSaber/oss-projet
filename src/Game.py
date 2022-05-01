from hashlib import new
import pygame
import re
from constants.Assets import Assets
from constants.Colors import Colors
from constants.Context import Context
from elements.Button import Button
from elements.Rectangle import Rectangle
from elements.MapImage import MapImage
from elements.Text import Text
import Saves
from json import load, dump
from typing import List, Tuple
import random

class Game:
    buttons: List[Button]
    texts: List[Text]
    rectangles: List[Rectangle]
    map_images: List[MapImage]
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
    map_images = []
    snake = []
    fruit = (0, 0)
    direction = 'up'
    speed = 75
    current_move = 'up'
    ranking = {"ranking": []}
    playing = bool
    gameover = False
    player = ''
    score = 0
    save_count = 0

    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.context = Context.MAIN_MENU
        self.create_main_menu_buttons()
        self.running = True
        self.background_image_surface = pygame.image.load(
            Assets.menu_background_image
        )
        self.load_settings()
        self.load_score()
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
                on_click=Button.to_ranking,
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

    def create_pause_menu_elements(self):
        self.texts.append(
            Text(
                font="Corbel",
                text="Pause",
                text_color=Colors.dark,
                text_position=(100, 250),
                text_size=35
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.pause_resume_game,
                rect=Rectangle(
                    position=(440, 100),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(400, 100),
                ),
                text=Text(
                    text="Resume",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(590, 130)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.pause_save_game,
                rect=Rectangle(
                    position=(440, 250),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(400, 100),
                ),
                text=Text(
                    text="Save",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(610, 280)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.pause_restart_game,
                rect=Rectangle(
                    position=(440, 400),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(400, 100),
                ),
                text=Text(
                    text="Restart",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(600, 430)
                ),
            )
        )
        self.buttons.append(
                    Button(
                        on_click=Button.pause_quit_game,
                        rect=Rectangle(
                            position=(440, 550),
                            color=(Colors.beige),
                            hover_color=(Colors.white),
                            size=(400, 100),
                        ),
                        text=Text(
                            text="Quit",
                            font="Corbel",
                            text_color=Colors.dark,
                            text_size=35,
                            text_position=(610, 580)
                        ),
                    )
                )

    def to_pause_menu(self):
        self.context = Context.PAUSE
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.map_images.clear()
        self.create_pause_menu_elements()
        self.playing = False

    def create_loadable_saves_menu(self, save_list):
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
        for save in save_list:
            save_name_display = "Map: %s || Date: %s" % (save[0].upper(), save[1].strftime("%m/%d/%Y, %H:%M:%S"))
            self.buttons.append(
                Button(
                    on_click=Button.play_this_save,
                    rect=Rectangle(
                        position=(100, y),
                        color=(Colors.beige),
                        hover_color=(Colors.white),
                        size=(880, 100),
                    ),
                    text=Text(
                        text=save_name_display,
                        font="Corbel",
                        text_color=Colors.dark,
                        text_size=35,
                        text_position=(120, y + 30)
                    ),
                    metadata=save[0]
                )
            )

            self.buttons.append(
                Button(
                    on_click=Button.delete_save,
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
                    metadata=save[0]
                )
            )

            y+= 120

    def display_map(self):
        if self.snake == None:
            return
        self.texts.clear()
        start_x = (1280-(17*40))/2
        start_y = ((720-(17*40))/2)
        self.map_images.append(MapImage(start_x + 17 * self.fruit[0], start_y + 17 * self.fruit[1], Assets.apple_image))
        self.rectangles.append(
            Rectangle(
                position=(start_x, start_y),
                color=(Colors.white),
                hover_color=None,
                size=(17*40, 17*40),
            )
        )

        x = start_x + 17 * (self.snake[0]["x"])
        y = start_y + 17 * (self.snake[0]["y"])
        if self.snake[0]["y"] > self.snake[1]["y"]:
            self.map_images.append(MapImage(x, y, Assets.head_down))
        elif self.snake[0]["y"] < self.snake[1]["y"]:
            self.map_images.append(MapImage(x, y, Assets.head_up))
        elif self.snake[0]["x"] > self.snake[1]["x"]:
            self.map_images.append(MapImage(x, y, Assets.head_right))
        else:
            self.map_images.append(MapImage(x, y, Assets.head_left))

        for i, curr in enumerate(self.snake[1:]):
            i += 1
            x = start_x + 17 * (curr["x"])
            y = start_y + 17 * (curr["y"])
            prev = self.snake[i - 1]
            next = None
            if i + 1 < len(self.snake):
                next = self.snake[i + 1]

            if prev["y"] > curr["y"]: # from down
                if next == None:
                    self.map_images.append(MapImage(x, y, Assets.tail_up))
                elif curr["y"] > next["y"]:
                    self.map_images.append(MapImage(x, y, Assets.body_vertical))
                elif curr["x"] > next["x"]:
                    self.map_images.append(MapImage(x, y, Assets.body_bottomleft))
                else:
                    self.map_images.append(MapImage(x, y, Assets.body_bottomright))
            elif prev["y"] < curr["y"]: # from up
                if next == None:
                    self.map_images.append(MapImage(x, y, Assets.tail_down))
                elif curr["y"] < next["y"]:
                    self.map_images.append(MapImage(x, y, Assets.body_vertical))
                elif curr["x"] > next["x"]:
                    self.map_images.append(MapImage(x, y, Assets.body_topleft))
                else:
                    self.map_images.append(MapImage(x, y, Assets.body_topright))
            elif prev["x"] > curr["x"]: # from right
                if next == None:
                    self.map_images.append(MapImage(x, y, Assets.tail_left))
                elif curr["y"] < next["y"]:
                    self.map_images.append(MapImage(x, y, Assets.body_bottomright))
                elif curr["y"] > next["y"]:
                    self.map_images.append(MapImage(x, y, Assets.body_topright))
                else:
                    self.map_images.append(MapImage(x, y, Assets.body_horizontal))
            else: # from left
                if next == None:
                    self.map_images.append(MapImage(x, y, Assets.tail_right))
                elif curr["y"] < next["y"]:
                    self.map_images.append(MapImage(x, y, Assets.body_bottomleft))
                elif curr["y"] > next["y"]:
                    self.map_images.append(MapImage(x, y, Assets.body_topleft))
                else:
                    self.map_images.append(MapImage(x, y, Assets.body_horizontal))
        self.texts.append(
            Text(
                text="Score: %s" %self.score ,
                font="Corbel",
                text_color=Colors.black,
                text_size=25,
                text_position=(50, 50)
            ),
        )

    def to_ranking(self):
        self.context = Context.OPTIONS
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.map_images.clear()
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

        y = 125
        for score in self.ranking["ranking"]:
            self.rectangles.append(
                Rectangle(
                    position=(150, y),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(400, 50),
                ),
            )
            self.texts.append(
                Text(
                    text="%s: %s" %(score["name"], score["score"]),
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(170, y + 15)
                ),
            )
            y+= 60

    def player_name(self, event):
        if event.key == pygame.K_BACKSPACE and len(self.player) > 0:
            self.player = self.player[:-1]
        elif len(self.player) <= 10:
            self.player += event.unicode

    def check_buttons_click(self, position: Tuple[int, int]):
        for button in self.buttons:
            button.check_click(game=self, position=position)

    def draw_elements(self, position: Tuple[int, int]):
        for rect in self.rectangles:
            rect.draw(screen=self.screen, color=rect.color)
        for text in self.texts:
            text.draw(screen=self.screen)
        for img in self.map_images:
            img.draw(screen=self.screen)
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
        self.map_images.clear()
        self.create_options_menu_elements()

    def to_load(self):
        self.context = Context.LOAD_SAVE
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.map_images.clear()
        saves = Saves.list_saves()
        self.create_loadable_saves_menu(saves)

    def delete_save(self, save_name):
        Saves.delete_save(save_name)
        self.to_load()

    def play_game_from_load(self, save_name):
        self.context = Context.IN_GAME
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.map_images.clear()
        data = Saves.load_save(save_name)
        self.snake = data["snake"]
        self.direction = data["direction"]
        self.fruit = (data["fruit"]["x"], data["fruit"]["y"])
        self.score = (len(self.snake) - 3) * 10
        self.display_map()
        self.playing = True

    def spawn_fruit(self):
        x = round(random.randrange(0, 40))
        y = round(random.randrange(0, 40))
        for elem in self.snake:
            if elem["x"] == x and elem["y"] == y:
                return self.spawn_fruit()
        self.fruit = (x, y)

    def new_game(self):
        self.playing = True
        self.gameover = False
        self.score = 0
        self.snake = []
        self.direction = 'up'
        self.current_move = 'up'
        self.snake.append({"x": 40/2, "y": 40/2})
        self.snake.append({"x": 40/2, "y": 40/2+1})
        self.snake.append({"x": 40/2, "y": 40/2+2})
        self.context = Context.IN_GAME
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.map_images.clear()
        self.spawn_fruit()
        self.display_map()

    def to_main_menu(self):
        self.context = Context.MAIN_MENU
        self.gameover = False
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.map_images.clear()
        self.create_main_menu_buttons()

    def load_score(self):
        try:
            self.ranking = load(open(".ranking.json"))
            self.ranking["ranking"].sort(key=lambda x: x["score"], reverse=True)
        except Exception as e:
            ranking = {
                "ranking": []
            }
            ranking_file = open('.ranking.json', 'w')
            dump(ranking, ranking_file)

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
                "right": "right",
                "pause": "space"
            }
            settings_file = open('settings.json', 'w')
            dump(settings, settings_file)
            self.settings = settings
        self.music_volume = self.settings["music"] / 100
        self.effects_volume = self.settings["effects"] / 100

    def update_settings(self, key, value):
        self.settings[key] = value
        dump(self.settings, open('settings.json', 'w'))

    def move_head(self, newhead, cut_tail, grow):
        if grow:
            self.score += 10
        self.snake.insert(0, {"x": newhead[0], "y": newhead[1]})
        if cut_tail:
            self.snake.pop()

    def is_snake(self, x, y):
        for elem in self.snake:
            if elem["x"] == x and elem["y"] == y:
                return True
        return False

    def save_rank(self):
        if len(self.player) == 0:
            return
        if len(self.ranking["ranking"]) >= 10:
            self.ranking["ranking"].pop()
        self.ranking["ranking"].append({"name": self.player, "score": self.score})
        self.ranking["ranking"].sort(key=lambda x: x["score"], reverse=True)
        self.player = ''
        ranking_file = open('.ranking.json', 'w')
        dump(self.ranking, ranking_file)
        self.to_main_menu()

    def add_rank_button(self, high):
        x, y = self.screen.get_size()
        self.buttons.append(
            Button(
                on_click=Button.save_rank if high else Button.to_main_menu,
                rect=Rectangle(
                    position=(x/2, y/2 + 100),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(100, 50),
                ),
                text=Text(
                    text="Enter" if high else "Back",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(x/2 + 25, y/2 + 110)
                ),
            )
        )

    def loose(self, event):
        x, y = self.screen.get_size()
        self.context = Context.MAIN_MENU
        high = False
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.map_images.clear()
        self.texts.append(
            Text(
                font="Corbel",
                text="Gameover",
                text_color=Colors.black,
                text_position=(x/2 - 35, y/2 + 50),
                text_size=50
            )
        )
        self.texts.append(
            Text(
                text="Score: %s" %self.score ,
                font="Corbel",
                text_color=Colors.dark,
                text_size=50,
                text_position=(x/2 - 20, y/2 - 20)
            ),
        )
        try:
            if len(self.ranking['ranking']) < 10 or self.score > self.ranking["ranking"][-1]["score"]:
                high = True
                self.add_rank_button(high)
        except Exception as e:
            high = True
            self.add_rank_button(high)

        if not high:
            self.add_rank_button(high)
        if high:
            self.texts.append(
                Text(
                    text="Enter your name: %s" %self.score ,
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=50,
                    text_position=(x/2 - 100, y/2 - 300)
                ),
            )
            self.texts.append(
                Text(
                    text=self.player,
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=50,
                    text_position=(x/2 - 50, y/2 - 200)
                ),
            )


    def move_up(self):
        newhead = (self.snake[0]["x"], self.snake[0]["y"] - 1)
        if newhead[1] < 0 or self.is_snake(newhead[0], newhead[1]):
            self.gameover = True
            return
        if self.fruit[0] == newhead[0] and self.fruit[1] == newhead[1]:
            self.move_head(newhead, False, True)
            self.spawn_fruit()
        else:
            self.move_head(newhead, True, False)

    def move_down(self):
        newhead = (self.snake[0]["x"], self.snake[0]["y"] + 1)
        if newhead[1] >= 40 or self.is_snake(newhead[0], newhead[1]):
            self.gameover = True
            return
        if self.fruit[0] == newhead[0] and self.fruit[1] == newhead[1]:
            self.move_head(newhead, False, True)
            self.spawn_fruit()
        else:
            self.move_head(newhead, True, False)

    def move_left(self):
        newhead = (self.snake[0]["x"] - 1, self.snake[0]["y"])
        if newhead[0] < 0 or self.is_snake(newhead[0], newhead[1]):
            self.gameover = True
            return
        if self.fruit[0] == newhead[0] and self.fruit[1] == newhead[1]:
            self.move_head(newhead, False, True)
            self.spawn_fruit()
        else:
            self.move_head(newhead, True, False)

    def move_right(self):
        newhead = (self.snake[0]["x"] + 1, self.snake[0]["y"])
        if newhead[0] >= 40 or self.is_snake(newhead[0], newhead[1]):
            self.gameover = True
            return
        if self.fruit[0] == newhead[0] and self.fruit[1] == newhead[1]:
            self.move_head(newhead, False, True)
            self.spawn_fruit()
        else:
            self.move_head(newhead, True, False)

    def move_snake(self):
        if self.direction == 'up' and self.playing:
            self.move_up()
            self.current_move = 'up'
        if self.direction == 'down':
            self.move_down()
            self.current_move = 'down'
        if self.direction == 'left':
            self.move_left()
            self.current_move = 'left'
        if self.direction == 'right':
            self.move_right()
            self.current_move = 'right'

    def change_direction(self, key):
        if key == pygame.key.key_code(self.settings['left']) and self.current_move != 'right':
            self.direction = 'left'
        elif key == pygame.key.key_code(self.settings['right']) and self.current_move != 'left':
            self.direction = 'right'
        elif key == pygame.key.key_code(self.settings['up']) and self.current_move != 'down':
            self.direction = 'up'
        elif key == pygame.key.key_code(self.settings['down']) and self.current_move != 'up':
            self.direction = 'down'
        pygame.event.clear()

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

    def check_key_binding_input(self, event):
        if event.type == pygame.KEYDOWN:
            match self.context:
                case Context.OPTIONS_WAITING_INPUT_UP:
                    self.change_binding_up(pygame.key.name(event.key))
                case Context.OPTIONS_WAITING_INPUT_DOWN:
                    self.change_binding_down(pygame.key.name(event.key))
                case Context.OPTIONS_WAITING_INPUT_LEFT:
                    self.change_binding_left(pygame.key.name(event.key))
                case Context.OPTIONS_WAITING_INPUT_RIGHT:
                    self.change_binding_right(pygame.key.name(event.key))
                case Context.OPTIONS_WAITING_INPUT_PAUSE:
                    self.change_binding_pause(pygame.key.name(event.key))
