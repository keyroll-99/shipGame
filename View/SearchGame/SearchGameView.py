from Config import Config
from Connection.Connection import Connection
from Models.Position import Position
from UI.Controls.Button import Button
from UI.Models.ButtonConfig import ButtonConfig
from View.BaseView import BaseView
from View.SearchGame.GameList import GameList
from View.SearchGame.ServerListAction import ServerListAction


class SearchGameView(BaseView):
    gameList: GameList
    actionButtons: ServerListAction
    refreshButton: Button

    def __init__(self):
        self.gameList = GameList()
        self.actionButtons = ServerListAction(self)
        self.refreshButton = Button(ButtonConfig(
            "Refresh",
            Config.BACK_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Config.LIGHT_GREY_COLOR,
            Position(
                400,
                40,
                635,
                (Config.SCREEN_SIZE[1] / 2) - 200
            ),
            self.refresh
        ))
        self.viewObjects = [
            self.gameList,
            self.actionButtons,
            self.refreshButton
        ]

    def load(self):
        super().load()
        self.refresh()
        self.actionButtons.showError = False

    def refresh(self, *args):
        self.gameList.serverList.config.elements = Connection.send_request(Config.GAME_ROOM_CONTROLLER, "get-all")
