from Models.GameObject import GameObject
from ObjectManager import ObjectManager


class BaseView:
    viewObjects: list[GameObject] = []

    def load(self):
        for gameObject in self.viewObjects:
            ObjectManager.register_object(gameObject)

    def unload(self):
        for gameObject in self.viewObjects:
            ObjectManager.remove_object(gameObject.objectId)
