from elements.MapImage import MapImage
from constants.Assets import Assets
from constants.Screen import Screen

class Fruit:
    pos: tuple[int, int]

    def __init__(self, pos: tuple[int, int] = None):
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
            Screen.START_X + Screen.SQUARE_SIZE * self.pos[0],
            Screen.START_Y + Screen.SQUARE_SIZE * self.pos[1],
            Assets.apple_image
        )
    
    def set_pos(self, pos: tuple[int, int]):
        self.pos = pos
    
    def get_distance(self, snake_head: tuple[int, int]) -> int:
        return abs(self.pos[0] - snake_head[0]) + abs(self.pos[1] - snake_head[1])
