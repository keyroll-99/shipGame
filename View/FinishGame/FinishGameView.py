from Config import Config
from Connection.Connection import Connection
from EventQueue.EventQueueManager import EventQueueManager
from EventQueue.Events.ChangeViewEvent import ChangeViewEvent
from Models.Position import Position
from Store.GameStore import GameStore
from Store.PlayerStore import PlayerStore
from UI.Controls.Button import Button
from UI.Controls.Label import Label
from UI.Models.ButtonConfig import ButtonConfig
from UI.Models.LabelConfig import LabelConfig
from View import ViewNames
from View.BaseView import BaseView


class FinishGame(BaseView):
    resultLabel: Label
    returnToSearchButton: Button

    def __init__(self):
        self.resultLabel = Label(LabelConfig(
            "_",
            Config.DEFAULT_TEXT_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Position(
                100,
                100,
                100,
                300
            )
        ))

        self.returnToSearchButton = Button(ButtonConfig(
            "Back to menu",
            Config.DEFAULT_TEXT_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Config.GREY_COLOR,
            Position(
                300,
                75,
                150,
                200
            ),
            self.back_to_search
        ))

        self.viewObjects = [self.resultLabel, self.returnToSearchButton]

    def load(self):
        winning_player = GameStore.winning_player_name
        player_name = PlayerStore.name
        self.resultLabel.text = "You Won" if winning_player == player_name else "You lose"
        super().load()

    @staticmethod
    def back_to_search(e, t):
        game_name = GameStore.name
        player_name = PlayerStore.name

        Connection.send_request("game", "close", {
            "playerName": player_name,
            "gameName": game_name
        })

        EventQueueManager.publish_event(ChangeViewEvent(ViewNames.SEARCH_GAME))
