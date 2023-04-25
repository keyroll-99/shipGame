from Config import Config
from Models.Position import Position
from UI.Controls.Label import Label, LabelConfig
from View.BaseView import BaseView
from View.GameLobby.GameLobbyLogic import GameLobbyLogic


class GameLobbyView(BaseView):

    def __init__(self):
        label = Label(LabelConfig(
            "Waiting for other player",
            Config.DEFAULT_TEXT_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Position(
                200,
                45,
                Config.SCREEN_SIZE[0] // 2 - 100,
                Config.SCREEN_SIZE[1] // 2 - 150
            ),
        ))

        self.viewObjects = [
            label,
            GameLobbyLogic()
        ]

    def load(self):
        super().load()
