from Models.Position import Position


class LabelConfig(Position):
    color: tuple[int, int, int]
    text: str
    fontSize: int

    def __init__(self, text: str, color: tuple[int, int, int], fontSize: int, position: Position):
        super().__init__(position.width, position.height, position.top, position.left)
        self.text = text
        self.color = color
        self.fontSize = fontSize
