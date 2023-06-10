from View.BaseView import BaseView
from View.Game.GameBoard import GameBoard
from View.Game.GameLogic import GameLogic
from View.Game.MoveLabel import MoveLabel


class GameView(BaseView):
    def __init__(self):
        self.viewObjects = []

    def load(self):
        self.viewObjects.append(GameLogic())
        self.viewObjects.append(MoveLabel())
        self.viewObjects.append(GameBoard(False))
        self.viewObjects.append(GameBoard(True))
        super().load()
