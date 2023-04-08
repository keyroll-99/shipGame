from Models.Position import Position


class ListConfig(Position):
    backgroundColor: tuple[int, int, int]
    onClickColor: tuple[int, int, int]
    color: tuple[int, int, int]
    fontSize: int
    elements: list[str]

    def __init__(self, color: tuple[int, int, int],
                 fontSize: int,
                 backgroundColor: tuple[int, int, int],
                 onClickColor: tuple[int, int, int],
                 position: Position,
                 elements: list[str]
                 ):
        super().__init__(position.width, position.height, position.top, position.left)
        self.backgroundColor = backgroundColor
        self.color = color
        self.fontSize = fontSize
        self.onClickColor = onClickColor
        self.elements = elements
