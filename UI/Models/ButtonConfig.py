from Models.Position import Position


class ButtonConfig(Position):
    backgroundColor: tuple[int, int, int]
    color: tuple[int, int, int]
    text: str
    fontSize: int

    def __init__(self, text: str, color: tuple[int, int, int], fontSize: int, backgroundColor: tuple[int, int, int],position: Position):
        super().__init__(position.width, position.height, position.top, position.left)
        self.text = text
        self.color = color
        self.fontSize = fontSize
        self.backgroundColor = backgroundColor
