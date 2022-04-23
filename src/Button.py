class Button:
    def __init__(self,
                 position: tuple[int, int],
                 size: tuple[int, int],
                 color: tuple[int, int, int],
                 text: str,
                 on_click: function,
                 ):
        self.position = position
        self.size = size
        self.color = color
        self.text = text
        self.on_click = function
        return
