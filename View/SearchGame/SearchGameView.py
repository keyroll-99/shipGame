from View.BaseView import BaseView
from UI.Controls.Label import Label, LabelConfig
from UI.Controls.Input import Input as InputControl, InputConfig
from Models.Position import Position
from Config import Config
from View.SearchGame.GameList import GameList
from Connection.Connection import Connection
from View.SearchGame.ActionButtons import ActionButtons


class SearchGameView(BaseView):
    gameList: GameList
    actionButtons: ActionButtons

    def __init__(self):
        self.gameList = GameList()
        self.actionButtons = ActionButtons()

        self.viewObjects = [
            self.gameList,
            self.actionButtons
        ]

    def load(self):
        super().load()
        self.gameList.serverList.config.elements = ["server-1", "server-2"]
        # todo change it wich server connection
        # self.gameList.serverList.config.elements = Connection.send_request(Config.GAME_ROOM_CONTROLLER, "get-all")
