from Config import Config
from Connection.Connection import Connection
from Models.GameObject import GameObject
from Store.GameStore import GameStore
from Store.PlayerStore import PlayerStore


class GameLogic(GameObject):

    def render(self, window):
        result = Connection.send_request(Config.GAME_CONTROLLER, "get-game-data",
                                         {"gameName": GameStore.name, "playerName": PlayerStore.name})

        GameStore.set_game_data(result)
        if GameStore.game_phase == "init":
            #  prepear to game
            pass
        else:
            # game logic with tour separate
            pass
