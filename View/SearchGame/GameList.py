from Config import Config
from Models.GameObject import GameObject
from Models.Position import Position
from UI.Controls.List import List, ListConfig
from Connection.Connection import Connection


class GameList(GameObject):
    serverList: List
    serverNames: list[str]

    def __init__(self):
        super().__init__(None)


        self.serverList = List(ListConfig(
            Config.BACK_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Config.GREY_COLOR,
            (255, 0, 0),
            Position(
                200,
                Config.SCREEN_SIZE[1],
                0,
                0
            ),
            ["test", "test2"]
        ))

    def render(self, window):
        self.serverList.render(window)
