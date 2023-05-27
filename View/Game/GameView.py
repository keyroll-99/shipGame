import Config.Config
from Models.Position import Position
from UI.Controls.Label import Label
from UI.Models.LabelConfig import LabelConfig
from View.BaseView import BaseView


class GameView(BaseView):
    def __init__(self):
        l = Label(LabelConfig(
            "dupa",
            Config.Config.BACK_COLOR,
            Config.Config.DEFAULT_FONT_SIZE,
            Position(
                100,
                100,
                100,
                100
            )
        ))
        self.viewObjects = [l]

    def load(self):
        super().load()
