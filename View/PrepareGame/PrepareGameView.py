from pygame.event import Event

from Connection.Connection import Connection
from Models.Position import Position
from Store.GameStore import GameStore
from Store.PlayerStore import PlayerStore
from UI.Controls.Button import Button
from UI.Controls.Label import Label
from UI.Models.ButtonConfig import ButtonConfig
from UI.Models.LabelConfig import LabelConfig
from View.BaseView import BaseView
from Config import Config
from View.PrepareGame.GameLogic import GameLogic


class PrepareGameView(BaseView):
    viewObjects = []

    board_cell_size = 49

    current_ship_info: Label
    current_ship_length = 5
    current_set_length = 0

    current_user_map = []
    map_buttons = []

    play_button: Button
    reset_button: Button

    def __init__(self):
        self.viewObjects = [
            GameLogic(self)
        ]

        for i in range(10):
            empty_arr = [None] * 10
            self.current_user_map.append(empty_arr)
        self.add_ships_lefts_label()
        self.render_board()
        self.reset_button_redner()
        self.render_play_button()

    def render_board(self):
        for y in range(10):
            self.map_buttons.append([])
            for x in range(10):
                self.map_buttons[y].append(
                    Button(ButtonConfig(
                        "",
                        Config.DEFAULT_TEXT_COLOR,
                        Config.DEFAULT_FONT_SIZE,
                        Config.BACK_COLOR,
                        Position(
                            self.board_cell_size,
                            self.board_cell_size,
                            150 + (y * self.board_cell_size) + y,
                            150 + (x * self.board_cell_size) + x
                        ),
                        self.on_button_click,
                        {"x": x, "y": y}
                    ))
                )
                self.viewObjects.append(self.map_buttons[y][x])

    def on_button_click(self, event: Event, target: Button):
        if self.current_ship_length > 0:
            meta_data = target.metaData
            x, y = meta_data["x"], meta_data["y"]
            if self.can_change_state(x, y, self.current_ship_length):
                target.backgroundColor = Config.GREY_COLOR
                self.current_user_map[y][x] = self.current_ship_length

                self.current_set_length += 1
                if self.current_set_length >= self.current_ship_length:
                    self.current_set_length = 0
                    self.current_ship_length -= 1
                    if self.current_ship_length > 0:
                        self.current_ship_info.text = f"Set ship with length {self.current_ship_length}"
                    else:
                        self.current_ship_info.text = f"Now you can play"
                        self.play_button.set_disabled_button(False)

    def can_change_state(self, x, y, current_symbol):
        if self.current_user_map[y][x] is None:
            if x > 0 and (self.current_user_map[y][x - 1] is not None \
                          and self.current_user_map[y][x - 1] != current_symbol):
                return False

            if x < 9 and (self.current_user_map[y][x + 1] is not None and \
                          self.current_user_map[y][x + 1] != current_symbol):
                return False

            if y > 0 and (self.current_user_map[y - 1][x] is not None \
                          and self.current_user_map[y - 1][x] != current_symbol):
                return False

            if y < 9 and (self.current_user_map[y + 1][x] is not None and \
                          self.current_user_map[y + 1][x] != current_symbol):
                return False

            if self.current_set_length > 0:
                result = False
                if x > 0 and self.current_user_map[y][x - 1] == current_symbol:
                    result = True

                if x < 9 and self.current_user_map[y][x + 1] == current_symbol:
                    result = True

                if y > 0 and self.current_user_map[y - 1][x] == current_symbol:
                    result = True

                if y < 9 and self.current_user_map[y + 1][x] == current_symbol:
                    result = True
                return result
            else:
                return True

        return False

    def add_ships_lefts_label(self):
        self.current_ship_info = Label(LabelConfig(
            f"Set ship with length {self.current_ship_length}",
            Config.DEFAULT_TEXT_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Position(
                200,
                45,
                100,
                150
            ),
        ))

        self.viewObjects.append(self.current_ship_info)

    def reset_button_redner(self):
        self.reset_button = Button(ButtonConfig(
            "Reset",
            Config.DEFAULT_TEXT_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Config.GREY_COLOR,
            Position(
                200,
                45,
                650,
                150
            ),
            self.reset_all
        ))
        self.viewObjects.append(self.reset_button)

    def reset_all(self, e: Event, t: Button):
        for y in range(10):
            for x in range(10):
                self.map_buttons[y][x].backgroundColor = Config.BACK_COLOR
                self.current_user_map[y][x] = None
                self.current_ship_length = 5
                self.current_set_length = 0
                self.current_ship_info.text = f"Set ship with length {self.current_ship_length}"

    def render_play_button(self):

        self.play_button = Button(ButtonConfig(
            "Play",
            Config.DEFAULT_TEXT_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Config.GREY_COLOR,
            Position(
                200,
                45,
                650,
                450
            ),
            self.play
        ))
        self.play_button.set_disabled_button(True)
        self.viewObjects.append(self.play_button)

    def play(self, e: Event, t: Button):
        result = Connection.send_request(Config.GAME_CONTROLLER, "ready", {
            "playerName": PlayerStore.name,
            "gameName": GameStore.name,
            "playerBoard": self.current_user_map
        })
        if result['isSuccess']:
            self.play_button.set_disabled_button(True)
            self.play_button.text = "Waiting..."
            self.reset_button.set_disabled_button(True)

