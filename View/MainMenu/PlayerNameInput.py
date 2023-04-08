from Models.GameObject import GameObject
from Models.Position import Position
from UI.Controls.Input import Input, InputConfig
from UI.Controls.Label import Label, LabelConfig
from Config import Config


class PlayerNameInput(GameObject):
    playerNameInput: Input
    playerNameLabel: Label
    errorLabel: Label
    showError: bool = False

    def __init__(self):
        super().__init__(None)
        self.playerNameLabel = Label(LabelConfig(
            "Enter your name: ",
            Config.DEFAULT_TEXT_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Position(
                300,
                30,
                Config.SCREEN_SIZE[0] / 2 - 100,
                Config.SCREEN_SIZE[1] / 2 - 250
            )
        ))

        self.playerNameInput = Input(InputConfig(
            Config.BACK_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Config.GREY_COLOR,
            Position(
                200,
                40,
                Config.SCREEN_SIZE[0] / 2 - 95,
                Config.SCREEN_SIZE[1] / 2
            )
        ))

        self.errorLabel = Label(LabelConfig(
            "Please fill name",
            Config.RED_COLOR,
            15,
            Position(
                300,
                30,
                Config.SCREEN_SIZE[0] / 2 - 50,
                Config.SCREEN_SIZE[1] / 2
            )
        ))

        self.eventsReaction = {**self.playerNameInput.eventsReaction, **self.playerNameInput.eventsReaction}

    def render(self, window):
        self.playerNameLabel.render(window)
        self.playerNameInput.render(window)
        if self.showError:
            self.errorLabel.render(window)
