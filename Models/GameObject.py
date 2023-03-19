from Models.Position import Position


class GameObject:
    __maxObjectId = 1
    position: Position
    objectId: int
    eventsReaction: dict = {}

    def __init__(self, position: Position):
        self.position = position
        self.objectId = GameObject.__maxObjectId
        GameObject.__maxObjectId += 1

    def render(self, window):
        raise NotImplemented("Not implemented")
