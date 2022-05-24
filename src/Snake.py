from typing import List
from elements.MapImage import MapImage
from constants.Assets import Assets
from constants.Screen import Screen
import pygame

class Snake:
    score: int
    snake: List[dict]
    direction: str
    current_move: str

    keys: dict

    is_bot = False

    def __init__(self, direction: str = 'up', init_snake: List[dict] = [], keys: dict = None, is_bot: bool = False):
        self.direction = direction
        self.current_move = direction
        self.snake = init_snake
        self.is_bot = is_bot
        if is_bot:
            self.keys = None
        else:
            self.keys = keys
        self.score = (len(init_snake) - 3) * 10
    
    def set_current_move(self, direction: str):
        self.current_move = direction
    
    def set_direction(self, direction: str):
        self.direction = direction

    def get_body_imgs(self) -> List[MapImage]:
        res: List[MapImage] = []

        x = Screen.START_X + Screen.SQUARE_SIZE * (self.snake[0]["x"])
        y = Screen.START_Y + Screen.SQUARE_SIZE * (self.snake[0]["y"])
        if self.snake[0]["y"] > self.snake[1]["y"]:
            res.append(MapImage(x, y, Assets.head_down))
        elif self.snake[0]["y"] < self.snake[1]["y"]:
            res.append(MapImage(x, y, Assets.head_up))
        elif self.snake[0]["x"] > self.snake[1]["x"]:
            res.append(MapImage(x, y, Assets.head_right))
        else:
            res.append(MapImage(x, y, Assets.head_left))

        for i, curr in enumerate(self.snake[1:]):
            i += 1
            x = Screen.START_X + Screen.SQUARE_SIZE * (curr["x"])
            y = Screen.START_Y + Screen.SQUARE_SIZE * (curr["y"])
            prev = self.snake[i - 1]
            next = None
            if i + 1 < len(self.snake):
                next = self.snake[i + 1]

            if prev["y"] > curr["y"]: # from down
                if next == None:
                    res.append(MapImage(x, y, Assets.tail_up))
                elif curr["y"] > next["y"]:
                    res.append(MapImage(x, y, Assets.body_vertical))
                elif curr["x"] > next["x"]:
                    res.append(MapImage(x, y, Assets.body_bottomleft))
                else:
                    res.append(MapImage(x, y, Assets.body_bottomright))
            elif prev["y"] < curr["y"]: # from up
                if next == None:
                    res.append(MapImage(x, y, Assets.tail_down))
                elif curr["y"] < next["y"]:
                    res.append(MapImage(x, y, Assets.body_vertical))
                elif curr["x"] > next["x"]:
                    res.append(MapImage(x, y, Assets.body_topleft))
                else:
                    res.append(MapImage(x, y, Assets.body_topright))
            elif prev["x"] > curr["x"]: # from right
                if next == None:
                    res.append(MapImage(x, y, Assets.tail_left))
                elif curr["y"] < next["y"]:
                    res.append(MapImage(x, y, Assets.body_bottomright))
                elif curr["y"] > next["y"]:
                    res.append(MapImage(x, y, Assets.body_topright))
                else:
                    res.append(MapImage(x, y, Assets.body_horizontal))
            else: # from left
                if next == None:
                    res.append(MapImage(x, y, Assets.tail_right))
                elif curr["y"] < next["y"]:
                    res.append(MapImage(x, y, Assets.body_bottomleft))
                elif curr["y"] > next["y"]:
                    res.append(MapImage(x, y, Assets.body_topleft))
                else:
                    res.append(MapImage(x, y, Assets.body_horizontal))
        return res
    
    def is_snake(self, pos: tuple[int, int]) -> bool:
        for elem in self.snake:
            if elem["x"] == pos[0] and elem["y"] == pos[1]:
                return True
        return False

    def move_head(self, newhead: tuple[int, int], grow: bool):
        if grow:
            self.score += 10
        self.snake.insert(0, {"x": newhead[0], "y": newhead[1]})
        if not grow:
            self.snake.pop()
    
    def get_head(self) -> tuple[int, int]:
        return (self.snake[0]["x"], self.snake[1]["y"])
    
    def get_available_next_heads(self) -> List[tuple[int, int]]:
        available_heads: List[tuple[int, int]] = []
        cur_head = (self.snake[0]["x"], self.snake[0]["y"])

        if cur_head[0] + 1 < 40 and not self.is_snake((cur_head[0] + 1, cur_head[1])):
            available_heads.append((cur_head[0] + 1, cur_head[1]))
        if cur_head[0] - 1 >= 0 and not self.is_snake((cur_head[0] - 1, cur_head[1])):
            available_heads.append((cur_head[0] - 1, cur_head[1]))
        if cur_head[1] + 1 < 40 and not self.is_snake((cur_head[0], cur_head[1] + 1)):
            available_heads.append((cur_head[0], cur_head[1] + 1))
        if cur_head[1] - 1 >= 0 and not self.is_snake((cur_head[0], cur_head[1] - 1)):
            available_heads.append((cur_head[0], cur_head[1] - 1))
        return available_heads

    def get_new_head(self, add_x: int, add_y: int) -> tuple[int, int]:
        return (self.snake[0]["x"] + add_x, self.snake[0]["y"] + add_y)
    
    def change_direction_keyboard(self, key):
        if self.is_bot:
            return
        if key == pygame.key.key_code(self.keys['left']) and self.current_move != 'right':
            self.direction = 'left'
        elif key == pygame.key.key_code(self.keys['right']) and self.current_move != 'left':
            self.direction = 'right'
        elif key == pygame.key.key_code(self.keys['up']) and self.current_move != 'down':
            self.direction = 'up'
        elif key == pygame.key.key_code(self.keys['down']) and self.current_move != 'up':
            self.direction = 'down'
        pygame.event.clear()
    
    def get_score(self) -> int:
        return self.score