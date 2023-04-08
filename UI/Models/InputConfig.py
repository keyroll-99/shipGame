from Models.Position import Position


class InputConfig(Position):
    backgroundColor: tuple[int, int, int]
    color: tuple[int, int, int]
    fontSize: int

    def __init__(self, color: tuple[int, int, int], fontSize: int, backgroundColor: tuple[int, int, int],
                 position: Position):
        super().__init__(position.width, position.height, position.top, position.left)
        self.color = color
        self.backgroundColor = backgroundColor
        self.fontSize = fontSize
