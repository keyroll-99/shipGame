from typing import Callable

from pygame.event import Event

from Models.Position import Position


class ButtonConfig(Position):
    backgroundColor: tuple[int, int, int]
    color: tuple[int, int, int]
    text: str
    fontSize: int
    onClick: Callable[[Event], None]
    metaData: dict

    def __init__(self, text: str, color: tuple[int, int, int], fontSize: int, backgroundColor: tuple[int, int, int],
                 position: Position, onClick: Callable, metaData = None):
        super().__init__(position.width, position.height, position.top, position.left)
        self.text = text
        self.color = color
        self.fontSize = fontSize
        self.backgroundColor = backgroundColor
        self.onClick = onClick
        if metaData is not None:
            self.metaData = metaData
        else:
            self.metaData = {}
