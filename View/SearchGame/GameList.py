from Config import Config
from Models.GameObject import GameObject
from Models.Position import Position
from UI.Controls.List import List, ListConfig


class GameList(GameObject):
    serverList: List
    serverNames: list[str]

    def __init__(self):
        super().__init__()

        self.serverList = List(ListConfig(
            Config.BACK_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Config.GREY_COLOR,
            Config.GRASS_GREY,
            Position(
                400,
                600,
                10,
                (Config.SCREEN_SIZE[1] / 2) - 200
            ),
            []
        ))

        self.eventsReaction = {**self.serverList.eventsReaction}

    def render(self, window):
        self.serverList.render(window)
