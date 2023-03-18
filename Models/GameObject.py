from Models.Position import Position
from UI.Exceptions.InvalidUiConfigException import InvalidUiConfigException
from pygame.event import Event


class GameObject:
    __maxObjectId = 0

    position: Position
    eventsReaction: dict = {}
    objectId: int

    def __init__(self, position: Position):
        InvalidUiConfigException.throw_if_invalid(position)
        self.position = position
        self.objectId = GameObject.__maxObjectId
        GameObject.__maxObjectId += 1

    def render(self, window):
        raise NotImplemented("Not implemented")
