from View.BaseView import BaseView
from UI.Controls.Label import Label, LabelConfig
from UI.Controls.Input import Input as InputControl, InputConfig
from Models.Position import Position
from Config import Config
from View.SearchGame.GameList import GameList
from Connection.Connection import Connection


class SearchGameView(BaseView):
    gameList: GameList

    def __init__(self):
        label = Label(LabelConfig("search game".upper(), (0, 0, 0), 40,
                                  Position(200, 10, Config.SCREEN_SIZE[0] / 2 - 200, Config.SCREEN_SIZE[1] / 2 - 125)))
        self.gameList = GameList()
        self.viewObjects = [
            label,
            self.gameList
        ]

    def load(self):
        super().load()
        self.gameList.serverList.config.elements = Connection.send_request(Config.GAME_ROOM_CONTROLLER, "get-all")
