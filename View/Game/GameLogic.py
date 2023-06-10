from Config import Config
from Connection.Connection import Connection
from EventQueue.EventQueueManager import EventQueueManager
from EventQueue.Events.ChangeViewEvent import ChangeViewEvent
from Models.GameObject import GameObject
from Store.GameStore import GameStore
from Store.PlayerStore import PlayerStore
from View import ViewNames


class GameLogic(GameObject):
    def __init__(self):
        super().__init__()

    def render(self, window):
        is_your_tour = GameStore.player_turn_name == PlayerStore.name
        if not is_your_tour:
            result = Connection.send_request(Config.GAME_CONTROLLER, "get-game-data",
                                             {"gameName": GameStore.name, "playerName": PlayerStore.name})
            GameStore.set_game_data(result)
            if GameStore.game_phase == "exit":
                EventQueueManager.publish_event(ChangeViewEvent(ViewNames.SEARCH_GAME))

        if GameStore.game_phase == 'end':
            EventQueueManager.publish_event(ChangeViewEvent(ViewNames.FINISH_GAME))
