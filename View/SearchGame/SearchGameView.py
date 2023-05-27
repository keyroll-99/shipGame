from Config import Config
from Connection.Connection import Connection
from View.BaseView import BaseView
from View.SearchGame.GameList import GameList
from View.SearchGame.ServerListAction import ServerListAction


class SearchGameView(BaseView):
    gameList: GameList
    actionButtons: ServerListAction

    def __init__(self):
        self.gameList = GameList()
        self.actionButtons = ServerListAction(self)

        self.viewObjects = [
            self.gameList,
            self.actionButtons
        ]

    def load(self):
        super().load()
        self.gameList.serverList.config.elements = Connection.send_request(Config.GAME_ROOM_CONTROLLER, "get-all")
