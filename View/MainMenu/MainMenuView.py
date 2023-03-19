from Models.Position import Position
from UI.Controls.Button import Button, ButtonConfig
from UI.Controls.Label import Label, LabelConfig
from View.BaseView import BaseView
from Config import Config
from EventQueue.EventQueueManager import EventQueueManager
from EventQueue.EventsProcessing.ChangeViewEventProcessing import ChangeViewEvent
from View import ViewNames


class MainMenuView(BaseView):
    def __init__(self):
        self.__render_menu_actions()
        self.__render_title()

    def __render_title(self):
        title = Label(LabelConfig(Config.GAME_NAME, Config.DEFAULT_TEXT_COLOR, 40,
                                  Position(200, 10, Config.SCREEN_SIZE[0] / 2 - 200, Config.SCREEN_SIZE[1] / 2 - 100)))

        self.viewObjects.append(title)

    def __render_menu_actions(self):
        button = Button(ButtonConfig("Play", Config.DEFAULT_TEXT_COLOR, 30, (240, 240, 240),
                                     Position(200, 60, Config.SCREEN_SIZE[0] / 2 - 100, Config.SCREEN_SIZE[1] / 2 - 100),
                                     self.load_search_game_view))

        self.viewObjects.append(button)

    @staticmethod
    def load_search_game_view(e):
        EventQueueManager.publish_event(ChangeViewEvent(ViewNames.SEARCH_GAME))
