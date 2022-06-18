from hashlib import new
import pygame
import re
from constants.Assets import Assets
from constants.Colors import Colors
from constants.Context import Context
from constants.Screen import Screen
from elements.Button import Button
from elements.Rectangle import Rectangle
from elements.MapImage import MapImage
from elements.Text import Text
from Snake import Snake
from Fruit import Fruit
import Saves
from json import load, dump
from typing import List
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
    board_height: int
    board_width: int
    buttons = []
    texts = []
    rectangles = []
    map_images = []

    player = ''

    snakes: List[Snake]
    fruits: List[Fruit]

    final_score: int = 0

    speed = 60
    ranking = {"ranking": []}
    playing = bool
    gameover = False
    save_count = 0

    def __init__(self):
        self.screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
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

        self.snakes = []
        self.fruits = []

    def create_main_menu_buttons(self):
        self.buttons.append(
            Button(
                on_click=Button.new_game,
                rect=Rectangle(
                    position=(200, 25),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(400, 75),
                ),
                text=Text(
                    text="Play",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(350, 50)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.new_dual_game,
                rect=Rectangle(
                    position=(680, 25),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(400, 75),
                ),
                text=Text(
                    text="Dual Play",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(750, 50)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.new_game_autoplayer,
                rect=Rectangle(
                    position=(200, 125),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(880, 75),
                ),
                text=Text(
                    text="Autoplayer",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(640, 150)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.to_load,
                rect=Rectangle(
                    position=(200, 225),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(880, 75),
                ),
                text=Text(
                    text="Load",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(640, 250)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.to_options,
                rect=Rectangle(
                    position=(200, 325),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(880, 75),
                ),
                text=Text(
                    text="Options",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(640, 350)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.to_ranking,
                rect=Rectangle(
                    position=(200, 425),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(880, 75),
                ),
                text=Text(
                    text="Ranking",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(640, 450)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.quit,
                rect=Rectangle(
                    position=(200, 525),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(880, 75),
                ),
                text=Text(
                    text="Exit",
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(640, 550)
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
                text="Player 1:",
                text_color=Colors.dark,
                text_position=(350, 300),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Up",
                text_color=Colors.dark,
                text_position=(350, 350),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Down",
                text_color=Colors.dark,
                text_position=(350, 400),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Left",
                text_color=Colors.dark,
                text_position=(350, 450),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Right",
                text_color=Colors.dark,
                text_position=(350, 500),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Pause",
                text_color=Colors.dark,
                text_position=(350, 550),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Player 2:",
                text_color=Colors.dark,
                text_position=(800, 300),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Up",
                text_color=Colors.dark,
                text_position=(800, 350),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Down",
                text_color=Colors.dark,
                text_position=(800, 400),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Left",
                text_color=Colors.dark,
                text_position=(800, 450),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Right",
                text_color=Colors.dark,
                text_position=(800, 500),
                text_size=35
            )
        )
        self.texts.append(
            Text(
                font="Corbel",
                text="Pause",
                text_color=Colors.dark,
                text_position=(800, 550),
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
                    position=(450, 345),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["first_player_controls"]["up"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(500, 350)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_down,
                rect=Rectangle(
                    position=(450, 395),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["first_player_controls"]["down"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(500, 400)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_left,
                rect=Rectangle(
                    position=(450, 445),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["first_player_controls"]["left"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(500, 450)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_right,
                rect=Rectangle(
                    position=(450, 495),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["first_player_controls"]["right"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(500, 500)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_pause,
                rect=Rectangle(
                    position=(450, 545),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["first_player_controls"]["pause"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(500, 550)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_up_second,
                rect=Rectangle(
                    position=(900, 345),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["second_player_controls"]["up"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(950, 350)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_down_second,
                rect=Rectangle(
                    position=(900, 395),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["second_player_controls"]["down"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(950, 400)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_left_second,
                rect=Rectangle(
                    position=(900, 445),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["second_player_controls"]["left"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(950, 450)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_right_second,
                rect=Rectangle(
                    position=(900, 495),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["second_player_controls"]["right"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(950, 500)
                ),
            )
        )
        self.buttons.append(
            Button(
                on_click=Button.change_context_pause_second,
                rect=Rectangle(
                    position=(900, 545),
                    color=(Colors.beige),
                    hover_color=(Colors.white),
                    size=(160, 40),
                ),
                text=Text(
                    text=self.settings["second_player_controls"]["pause"],
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(950, 550)
                ),
            )
        )

    def create_pause_menu_elements(self, isDualGame: bool):
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
        if isDualGame:
            self.buttons.append(
                Button(
                    on_click=Button.pause_dual_restart_game,
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
        else:
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

    def to_pause_menu(self, isDualGame: bool):
        self.context = Context.PAUSE
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.map_images.clear()
        self.create_pause_menu_elements(isDualGame)
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
            save_name_display = "Map: %s || Date: %s" % (
                save[0].upper(), save[1].strftime("%m/%d/%Y, %H:%M:%S"))
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

            y += 120

    def display_map(self):
        if self.snakes == None or len(self.snakes) < 1:
            return
        self.texts.clear()
        self.board_height = Screen.BOARD_HEIGHT
        self.board_width = Screen.BOARD_WIDTH
        self.rectangles.append(
            Rectangle(
                position=(Screen.START_X, Screen.START_Y),
                color=(Colors.white),
                hover_color=None,
                size=(Screen.SQUARE_SIZE * Screen.BOARD_WIDTH,
                      Screen.SQUARE_SIZE * Screen.BOARD_HEIGHT),
            )
        )
        for snake in self.snakes:
            self.map_images += snake.get_body_imgs()
        for fruit in self.fruits:
            self.map_images.append(fruit.get_fruit_img())
        if self.context != Context.DUAL_GAME:
            self.display_scores()

    def display_dual_map(self):
        if self.snakes == None or len(self.snakes) < 1:
            return
        self.texts.clear()
        self.board_width = Screen.BOARD_WIDTH_DUAL
        self.board_height = Screen.BOARD_HEIGHT_DUAL
        self.rectangles.append(
            Rectangle(
                position=(Screen.START_X_DUAL, Screen.START_Y_DUAL),
                color=(Colors.white),
                hover_color=None,
                size=(Screen.SQUARE_SIZE * Screen.BOARD_WIDTH_DUAL,
                      Screen.SQUARE_SIZE * Screen.BOARD_HEIGHT_DUAL),
            )
        )
        for snake in self.snakes:
            self.map_images += snake.get_body_imgs()
        for fruit in self.fruits:
            self.map_images.append(fruit.get_fruit_img())
        if self.context != Context.DUAL_GAME:
            self.display_scores()

    def display_scores(self):
        self.texts.append(
            Text(
                text="Score: %s" % self.snakes[0].score,
                font="Corbel",
                text_color=Colors.black,
                text_size=25,
                text_position=(50, 50)
            ),
        )

        if len(self.snakes) == 2:
            self.texts.append(
                Text(
                    text="Score: %s" % self.snakes[1].score,
                    font="Corbel",
                    text_color=Colors.black,
                    text_size=25,
                    text_position=(1000, 50)
                ),
            )

    def move_snakes(self) -> tuple[bool, int]:
        for i, snake in enumerate(self.snakes):
            next_head: tuple[int, int]
            if snake.is_bot:
                next_head = self.find_bot_best_next_head(snake)
            else:
                next_head: tuple[int, int] = (0, 0)
                match snake.direction:
                    case 'up':
                        next_head = snake.get_new_head(0, -1)
                    case 'down':
                        next_head = snake.get_new_head(0, 1)
                    case 'left':
                        next_head = snake.get_new_head(-1, 0)
                    case 'right':
                        next_head = snake.get_new_head(1, 0)
                snake.set_current_move(snake.direction)
            if not self.move_snake(snake, next_head):
                return (False, i)
        return (True, -1)

    def move_snake(self, snake: Snake, newhead: tuple[int, int]):
        # snake out of map
        if newhead[0] < 0 or newhead[0] >= self.board_width or newhead[1] < 0 or newhead[1] >= self.board_height:
            return False

        # snake hits himself or another snake
        for snk in self.snakes:
            if snk.is_snake(newhead):
                return False

        # snake eats fruit
        eats = False
        for fruit in self.fruits:
            if fruit.is_fruit(newhead):
                snake.move_head(newhead, True)
                fruit.set_pos(self.generate_new_fruit_pos())
                eats = True

        # snake is not eating a fruit
        if not eats:
            snake.move_head(newhead, False)
        return True

    def generate_new_fruit_pos(self):
        if self.context == Context.DUAL_GAME:
            newpos = (round(random.randrange(0, 80)),
                      round(random.randrange(0, 40)))
        else:
            newpos = (round(random.randrange(0, 40)),
                      round(random.randrange(0, 40)))

        # check if there is a snake on newpos
        for snake in self.snakes:
            if snake.is_snake(newpos):
                return self.generate_new_fruit_pos()

        # check if there already is a fruit on newpos
        for fruit in self.fruits:
            if fruit.is_fruit(newpos):
                return self.generate_new_fruit_pos()
        return newpos

    def find_bot_best_next_head(self, snake: Snake) -> tuple[int, int]:
        nearest_fruit: Fruit = None
        shortest_dist: int = -1
        for fruit in self.fruits:
            dist = fruit.get_distance(snake.get_head())
            if shortest_dist == -1 or dist < shortest_dist:
                shortest_dist = dist
                nearest_fruit = fruit
        available_next_heads = snake.get_available_next_heads()
        shortest_dist = -1
        next_head: tuple[int, int] = None
        for available_next_head in available_next_heads:
            dist = nearest_fruit.get_distance(available_next_head)
            if shortest_dist == -1 or dist < shortest_dist:
                shortest_dist = dist
                next_head = available_next_head
        if shortest_dist == -1:
            return snake.get_new_head(0, 1)
        return next_head

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
                    text="%s: %s" % (score["name"], score["score"]),
                    font="Corbel",
                    text_color=Colors.dark,
                    text_size=35,
                    text_position=(170, y + 15)
                ),
            )
            y += 60

    def player_name(self, event):
        if event.key == pygame.K_BACKSPACE and len(self.player) > 0:
            self.player = self.player[:-1]
        elif len(self.player) <= 10:
            self.player += event.unicode

    def check_buttons_click(self, position: tuple[int, int]):
        for button in self.buttons:
            button.check_click(game=self, position=position)

    def draw_elements(self, position: tuple[int, int]):
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
        self.snakes.append(Snake(
            screen_start_x=Screen.START_X,
            screen_start_y=Screen.START_Y,
            sprites={
                "head_down": Assets.head_down,
                "head_up": Assets.head_up,
                "head_right": Assets.head_right,
                "head_left": Assets.head_left,
                "tail_down": Assets.tail_down,
                "tail_up": Assets.tail_up,
                "tail_right": Assets.tail_right,
                "tail_left": Assets.tail_left,
                "body_vertical": Assets.body_vertical,
                "body_horizontal": Assets.body_horizontal,
                "body_topright": Assets.body_topright,
                "body_topleft": Assets.body_topleft,
                "body_bottomright": Assets.body_bottomright,
                "body_bottomleft": Assets.body_bottomleft,
            },
            direction=data["direction"],
            init_snake=data["snake"],
            keys=self.settings["first_player_controls"]
        ))
        self.fruits.clear()
        self.fruits.append(
            Fruit(
                Screen.START_X,
                Screen.START_Y,
                (data["fruit"]["x"], data["fruit"]["y"])
            )
        )
        self.display_map()
        self.playing = True

    def new_game(self):
        self.playing = True
        self.gameover = False

        self.snakes.append(Snake(
            screen_start_x=Screen.START_X,
            screen_start_y=Screen.START_Y,
            sprites={
                "head_down": Assets.head_down,
                "head_up": Assets.head_up,
                "head_right": Assets.head_right,
                "head_left": Assets.head_left,
                "tail_down": Assets.tail_down,
                "tail_up": Assets.tail_up,
                "tail_right": Assets.tail_right,
                "tail_left": Assets.tail_left,
                "body_vertical": Assets.body_vertical,
                "body_horizontal": Assets.body_horizontal,
                "body_topright": Assets.body_topright,
                "body_topleft": Assets.body_topleft,
                "body_bottomright": Assets.body_bottomright,
                "body_bottomleft": Assets.body_bottomleft,
            },
            direction="up",
            init_snake=[
                {"x": 40/2, "y": 40/2},
                {"x": 40/2, "y": 40/2+1},
                {"x": 40/2, "y": 40/2+2}
            ],
            keys=self.settings["first_player_controls"]
        ))
        #issue 40
        self.fruits.clear()
        self.fruits.append(
            Fruit(
                Screen.START_X,
                Screen.START_Y,
                self.generate_new_fruit_pos()
            )
        )

        self.context = Context.IN_GAME
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.map_images.clear()
        self.display_map()

    def new_dual_game(self):
        self.playing = True
        self.gameover = False

        self.snakes.append(Snake(
            screen_start_x=Screen.START_X_DUAL,
            screen_start_y=Screen.START_Y_DUAL,
            sprites={
                "head_down": Assets.head_down,
                "head_up": Assets.head_up,
                "head_right": Assets.head_right,
                "head_left": Assets.head_left,
                "tail_down": Assets.tail_down,
                "tail_up": Assets.tail_up,
                "tail_right": Assets.tail_right,
                "tail_left": Assets.tail_left,
                "body_vertical": Assets.body_vertical,
                "body_horizontal": Assets.body_horizontal,
                "body_topright": Assets.body_topright,
                "body_topleft": Assets.body_topleft,
                "body_bottomright": Assets.body_bottomright,
                "body_bottomleft": Assets.body_bottomleft,
            },
            direction="down",
            init_snake=[
                {"x": 2, "y": 3},
                {"x": 2, "y": 2},
                {"x": 2, "y": 1}
            ],
            keys=self.settings["first_player_controls"]
        ))

        self.snakes.append(Snake(
            screen_start_x=Screen.START_X_DUAL,
            screen_start_y=Screen.START_Y_DUAL,
            sprites={
                "head_down": Assets.head_down_second,
                "head_up": Assets.head_up_second,
                "head_right": Assets.head_right_second,
                "head_left": Assets.head_left_second,
                "tail_down": Assets.tail_down_second,
                "tail_up": Assets.tail_up_second,
                "tail_right": Assets.tail_right_second,
                "tail_left": Assets.tail_left_second,
                "body_vertical": Assets.body_vertical_second,
                "body_horizontal": Assets.body_horizontal_second,
                "body_topright": Assets.body_topright_second,
                "body_topleft": Assets.body_topleft_second,
                "body_bottomright": Assets.body_bottomright_second,
                "body_bottomleft": Assets.body_bottomleft_second,
            },
            direction="up",
            init_snake=[
                {"x": 78, "y": 37},
                {"x": 78, "y": 38},
                {"x": 78, "y": 39}
            ],
            keys=self.settings["second_player_controls"]
        ))
        self.fruits.append(
            Fruit(
                Screen.START_X_DUAL,
                Screen.START_Y_DUAL,
                self.generate_new_fruit_pos()
            )
        )
        self.fruits.append(
            Fruit(
                Screen.START_X_DUAL,
                Screen.START_Y_DUAL,
                self.generate_new_fruit_pos()
            )
        )

        self.context = Context.DUAL_GAME
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.map_images.clear()
        self.display_dual_map()

    def new_game_autoplayer(self):
        self.playing = True
        self.gameover = False

        self.snakes.append(Snake(
            screen_start_x=Screen.START_X,
            screen_start_y=Screen.START_Y,
            sprites={
                "head_down": Assets.head_down,
                "head_up": Assets.head_up,
                "head_right": Assets.head_right,
                "head_left": Assets.head_left,
                "tail_down": Assets.tail_down,
                "tail_up": Assets.tail_up,
                "tail_right": Assets.tail_right,
                "tail_left": Assets.tail_left,
                "body_vertical": Assets.body_vertical,
                "body_horizontal": Assets.body_horizontal,
                "body_topright": Assets.body_topright,
                "body_topleft": Assets.body_topleft,
                "body_bottomright": Assets.body_bottomright,
                "body_bottomleft": Assets.body_bottomleft,
            },
            direction="up",
            init_snake=[
                {"x": 39, "y": 37},
                {"x": 39, "y": 38},
                {"x": 39, "y": 39}
            ],
            is_bot=True
        ))
        self.fruits.append(
            Fruit(
                Screen.START_X,
                Screen.START_Y,
                self.generate_new_fruit_pos()
            )
        )

        self.context = Context.IN_GAME
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.map_images.clear()
        self.display_map()

    def to_main_menu(self):
        self.context = Context.MAIN_MENU
        self.gameover = False
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.map_images.clear()
        self.snakes.clear()
        self.fruits.clear()
        self.final_score = 0
        self.playing = False
        self.create_main_menu_buttons()

    def load_score(self):
        try:
            self.ranking = load(open(".ranking.json"))
            self.ranking["ranking"].sort(
                key=lambda x: x["score"], reverse=True)
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
                "first_player_controls": {
                    "up": "w",
                    "down": "s",
                    "left": "a",
                    "right": "d",
                    "pause": "escape"
                },
                "second_player_controls": {
                    "up": "up",
                    "down": "down",
                    "left": "left",
                    "right": "right",
                    "pause": "return"
                },
            }
            settings_file = open('settings.json', 'w')
            dump(settings, settings_file)
            self.settings = settings
        self.music_volume = self.settings["music"] / 100
        self.effects_volume = self.settings["effects"] / 100

    def update_settings(self, key, value, path=None):
        if path:
            self.settings[path][key] = value
        else:
            self.settings[key] = value
        dump(self.settings, open('settings.json', 'w'))

    def save_rank(self):
        if len(self.player) == 0:
            return
        if len(self.ranking["ranking"]) >= 10:
            self.ranking["ranking"].pop()
        self.ranking["ranking"].append(
            {"name": self.player, "score": self.final_score})
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

    def loose(self, is_bot):
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
                text="Score: %s" % self.final_score,
                font="Corbel",
                text_color=Colors.dark,
                text_size=50,
                text_position=(x/2 - 20, y/2 - 20)
            ),
        )
        if not is_bot:
            try:
                if len(self.ranking['ranking']) < 10 or self.final_score > self.ranking["ranking"][-1]["score"]:
                    high = True
                    self.add_rank_button(high)
            except Exception as e:
                high = True
                self.add_rank_button(high)

            if high:
                self.texts.append(
                    Text(
                        text="Enter your name: %s" % self.final_score,
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
            else:
                self.add_rank_button(high)
        else:
            self.add_rank_button(False)

    def change_binding_up(self, key):
        if not self.check_binding_used(key):
            self.update_settings("up", key, "first_player_controls")
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_down(self, key):
        if not self.check_binding_used(key):
            self.update_settings("down", key, "first_player_controls")
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_left(self, key):
        if not self.check_binding_used(key):
            self.update_settings("left", key, "first_player_controls")
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_right(self, key):
        if not self.check_binding_used(key):
            self.update_settings("right", key, "first_player_controls")
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_pause(self, key):
        if not self.check_binding_used(key):
            self.update_settings("pause", key, "first_player_controls")
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_up_second(self, key):
        if not self.check_binding_used(key):
            self.update_settings("up", key, "second_player_controls")
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_down_second(self, key):
        if not self.check_binding_used(key):
            self.update_settings("down", key, "second_player_controls")
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_left_second(self, key):
        if not self.check_binding_used(key):
            self.update_settings("left", key, "second_player_controls")
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_right_second(self, key):
        if not self.check_binding_used(key):
            self.update_settings("right", key, "second_player_controls")
        self.buttons.clear()
        self.rectangles.clear()
        self.texts.clear()
        self.create_options_menu_elements()
        self.context = Context.OPTIONS
        return

    def change_binding_pause_second(self, key):
        if not self.check_binding_used(key):
            self.update_settings("pause", key, "second_player_controls")
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
                case Context.OPTIONS_WAITING_INPUT_UP_SECOND:
                    self.change_binding_up_second(pygame.key.name(event.key))
                case Context.OPTIONS_WAITING_INPUT_DOWN_SECOND:
                    self.change_binding_down_second(pygame.key.name(event.key))
                case Context.OPTIONS_WAITING_INPUT_LEFT_SECOND:
                    self.change_binding_left_second(pygame.key.name(event.key))
                case Context.OPTIONS_WAITING_INPUT_RIGHT_SECOND:
                    self.change_binding_right_second(
                        pygame.key.name(event.key))
                case Context.OPTIONS_WAITING_INPUT_PAUSE_SECOND:
                    self.change_binding_pause_second(
                        pygame.key.name(event.key))

    def check_binding_used(self, new_key):
        for key in self.settings["first_player_controls"]:
            if (self.settings["first_player_controls"][key] == new_key):
                return True
        for key in self.settings["second_player_controls"]:
            if (self.settings["second_player_controls"][key] == new_key):
                return True
        return False
