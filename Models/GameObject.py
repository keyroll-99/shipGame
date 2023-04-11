from Models.Position import Position
import pygame


class GameObject:
    __maxObjectId = 1
    position: Position
    objectId: int
    eventsReaction: dict = {}

    def __init__(self, position: Position | None = None):
        self.position = position
        self.objectId = GameObject.__maxObjectId
        GameObject.__maxObjectId += 1

    def render(self, window):
        raise NotImplemented("Not implemented")

    def is_mouse_over(self) -> bool:
        mouse_position = pygame.mouse.get_pos()

        return self.position.left < mouse_position[0] < self.position.left + self.position.width \
            and self.position.top < mouse_position[1] < self.position.top + self.position.height
