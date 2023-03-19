from View.BaseView import BaseView
from UI.Controls.Label import Label, LabelConfig
from Models.Position import Position
from Config import Config


class SearchGameView(BaseView):
    def __init__(self):
        label = Label(LabelConfig("search game".upper(), (0, 0, 0), 40,
                                  Position(200, 10, Config.SCREEN_SIZE[0] / 2 - 200, Config.SCREEN_SIZE[1] / 2 - 125)))

        self.viewObjects = [
            label
        ]
