from Config import Config
from EventQueue.EventQueueManager import EventQueueManager
from EventQueue.Events.CloseGameEvent import CloseGameEvent
from EventQueue.EventsProcessing.ChangeViewEventProcessing import ChangeViewEvent
from Models.Position import Position
from UI.Controls.Button import Button, ButtonConfig
from UI.Controls.Label import Label, LabelConfig
from View import ViewNames
from View.BaseView import BaseView
from View.MainMenu.PlayerNameInput import PlayerNameInput
from Connection.Connection import Connection
from Store.PlayerStore import PlayerStore


class MainMenuView(BaseView):
    playerNameInput: PlayerNameInput

    def __init__(self):
        self.viewObjects = []
        self.__render_menu_actions()
        self.__render_title()

    def __render_title(self):
        title = Label(LabelConfig(Config.GAME_NAME, Config.DEFAULT_TEXT_COLOR, 40,
                                  Position(200, 10, Config.SCREEN_SIZE[0] / 2 - 200, Config.SCREEN_SIZE[1] / 2 - 100)))

        self.viewObjects.append(title)

    def __render_menu_actions(self):
        self.playerNameInput = PlayerNameInput()

        play_button = Button(ButtonConfig("Play",
                                          Config.DEFAULT_TEXT_COLOR,
                                          30,
                                          Config.LIGHT_GREY_COLOR,
                                          Position(
                                              200,
                                              60,
                                              Config.SCREEN_SIZE[0] / 2,
                                              Config.SCREEN_SIZE[1] / 2 - 100
                                          ),
                                          self.join_to_game))

        exit_button = Button(ButtonConfig("Exit",
                                          Config.DEFAULT_TEXT_COLOR,
                                          30,
                                          Config.LIGHT_GREY_COLOR,
                                          Position(
                                              200,
                                              60,
                                              Config.SCREEN_SIZE[0] / 2 + 100,
                                              Config.SCREEN_SIZE[1] / 2 - 100
                                          ),
                                          self.exit))

        self.viewObjects.append(play_button)
        self.viewObjects.append(exit_button)
        self.viewObjects.append(self.playerNameInput)

    def join_to_game(self, *args):
        if self.playerNameInput.playerNameInput.text == "":
            self.playerNameInput.showError = True
        else:
            player_name = self.playerNameInput.playerNameInput.text
            response = Connection.send_request(Config.PLAYER_CONTROLLER, "join", player_name)
            if not response["isSuccess"]:
                self.playerNameInput.errorLabel.text = response['message']
                self.playerNameInput.showError = True
            else:
                PlayerStore.name = player_name
                EventQueueManager.publish_event(ChangeViewEvent(ViewNames.SEARCH_GAME))

    @staticmethod
    def exit(*args):
        EventQueueManager.publish_event(CloseGameEvent())
