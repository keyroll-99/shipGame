from pygame import Surface, SurfaceType

from Models.GameObject import GameObject


class ObjectManager:
    __gameObjects: list[GameObject] = []

    @staticmethod
    def render_game_objects(window: Surface | SurfaceType):
        for gameObject in ObjectManager.__gameObjects:
            gameObject.render(window)

    @staticmethod
    def register_object(gameObject: GameObject):
        ObjectManager.__gameObjects.append(gameObject)

    @staticmethod
    def remove_object(objectId: int):
        ObjectManager.__gameObjects = list(filter(lambda x: x.objectId != objectId, ObjectManager.__gameObjects))

    @staticmethod
    def get_all_objects():
        return ObjectManager.__gameObjects

