from Models.GameObject import GameObject
from EventQueue.EventQueueManager import EventQueueManager
from EventQueue.Events.ChangeViewEvent import ChangeViewEvent
from Connection.Connection import Connection
from Config import Config
from Store.GameStore import GameStore
from View.ViewNames import PREPARE_GAME


class GameLobbyLogic(GameObject):

    def render(self, window):
        result = Connection.send_request(Config.GAME_CONTROLLER, "can-start", {"name": GameStore.name})
        if result["canStart"]:
            EventQueueManager.publish_event(ChangeViewEvent(PREPARE_GAME))
