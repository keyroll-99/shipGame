from View.BaseView import BaseView
from UI.Controls.Label import Label, LabelConfig
from Store.GameStore import GameStore
from Config import Config
from Models.Position import Position
from View.Game.GameLogic import GameLogic


class GameView(BaseView):
    def __init__(self):
        label = Label(LabelConfig(
            "gra",
            Config.BACK_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Position(
                100,
                100,
                250,
                250
            )
        ))

        game_logic = GameLogic()

        self.viewObjects = [label, game_logic]

    def load(self):
        super().load()
