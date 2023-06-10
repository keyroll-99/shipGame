from Config import Config
from Models.GameObject import GameObject
from Models.Position import Position
from Store.GameStore import GameStore
from Store.PlayerStore import PlayerStore
from UI.Controls.Label import Label
from UI.Models.LabelConfig import LabelConfig


class MoveLabel(GameObject):
    label: Label

    def __init__(self):
        super().__init__()
        is_player_turn = GameStore.player_turn_name == PlayerStore.name

        self.label = Label(LabelConfig(
            "Your turn" if is_player_turn else "Enemy turn",
            Config.DEFAULT_TEXT_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Position(
                100,
                100,
                100,
                250
            )
        ))

    def render(self, window):
        is_player_turn = GameStore.player_turn_name == PlayerStore.name
        self.label.text = "Your turn" if is_player_turn else "Enemy turn"

        self.label.render(window)
