from Config import Config
from Connection.Connection import Connection
from EventQueue.EventQueueManager import EventQueueManager
from EventQueue.Events.ChangeViewEvent import ChangeViewEvent
from Models.GameObject import GameObject
from Store.GameStore import GameStore
from Store.PlayerStore import PlayerStore
from View import ViewNames


class GameLogic(GameObject):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def render(self, window):
        result = Connection.send_request(Config.GAME_CONTROLLER, "get-game-data",
                                         {"gameName": GameStore.name, "playerName": PlayerStore.name})

        GameStore.set_game_data(result)
        if GameStore.game_phase != "init":
            EventQueueManager.publish_event(ChangeViewEvent(ViewNames.GAME))
            pass
