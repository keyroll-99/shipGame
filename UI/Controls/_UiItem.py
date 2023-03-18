from Models.Position import Position
from UI.Exceptions.InvalidUiConfigException import InvalidUiConfigException


class UiItem:
    config: Position

    def __init__(self, position: Position):
        InvalidUiConfigException.throw_if_invalid(position)
        self.position = position

    def render(self, window):
        raise NotImplemented("Not implemented")
