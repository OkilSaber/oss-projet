from elements.MapImage import MapImage
from constants.Assets import Assets
from constants.Screen import Screen


class Fruit:
    pos: tuple[int, int]
    screen_start_x: int
    screen_start_y: int

    def __init__(self, screen_start_x: int, screen_start_y: int, pos: tuple[int, int] = None):
        self.screen_start_x = screen_start_x
        self.screen_start_y = screen_start_y
        if pos is None:
            self.pos = (0, 0)
        else:
            self.pos = pos

    def get_pos(self):
        return self.pos

    def is_fruit(self, pos: tuple[int, int]):
        return self.pos[0] == pos[0] and self.pos[1] == pos[1]

    def get_fruit_img(self):
        return MapImage(
            self.screen_start_x + Screen.SQUARE_SIZE * self.pos[0],
            self.screen_start_y + Screen.SQUARE_SIZE * self.pos[1],
            Assets.apple_image
        )

    def set_pos(self, pos: tuple[int, int]):
        self.pos = pos

    def get_distance(self, snake_head: tuple[int, int]) -> int:
        return abs(self.pos[0] - snake_head[0]) + abs(self.pos[1] - snake_head[1])
