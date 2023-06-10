import pygame
from pygame.event import Event

from Config import Config
from Connection.Connection import Connection
from Models.GameObject import GameObject
from Models.Position import Position
from Store.GameStore import GameStore
from Store.PlayerStore import PlayerStore
from UI.Controls.Button import Button
from UI.Models.ButtonConfig import ButtonConfig


class GameBoard(GameObject):
    buttons = []
    board_cell_size = 29
    leftPadding = 0

    def __init__(self, is_hit_board):
        super().__init__()
        self.is_hit_board = is_hit_board
        self.leftPadding = 100 if not is_hit_board else 450
        self.add_buttons()
        self.eventsReaction = {
            pygame.MOUSEBUTTONUP: self.on_mouse_button_up,
            pygame.MOUSEBUTTONDOWN: self.on_mouse_button_down
        }

    def on_mouse_button_up(self, e: Event):
        for row in self.buttons:
            for button in row:
                button.on_mouse_button_down(e)

    def on_mouse_button_down(self, e: Event):
        for row in self.buttons:
            for button in row:
                button.on_mouse_button_down(e)

    def add_buttons(self):
        for y in range(10):
            self.buttons.append([])
            for x in range(10):
                color = Config.BACK_COLOR
                if not self.is_hit_board and GameStore.enemy_hit[y][x] == 'x':
                    color = Config.RED_COLOR
                if not self.is_hit_board and GameStore.enemy_hit[y][x] == '-':
                    color = Config.GRASS_GREY
                elif self.is_hit_board and GameStore.player_hit[y][x] == "x":
                    color = Config.RED_COLOR
                elif self.is_hit_board and GameStore.player_hit[y][x] == "-":
                    color = Config.LIGHT_GREY_COLOR
                elif not self.is_hit_board and GameStore.player_board[y][x] is not None:
                    if GameStore.player_board[y][x] == "x":
                        color = Config.RED_COLOR
                    elif GameStore.player_board[y][x] == "-":
                        color = Config.BACK_COLOR
                    else:
                        color = Config.GREY_COLOR

                self.buttons[y].append(
                    Button(ButtonConfig(
                        "",
                        Config.DEFAULT_TEXT_COLOR,
                        Config.DEFAULT_FONT_SIZE,
                        color,
                        Position(
                            self.board_cell_size,
                            self.board_cell_size,
                            150 + (y * self.board_cell_size) + y,
                            self.leftPadding + (x * self.board_cell_size) + x
                        ),
                        self.on_button_click,
                        {"x": x, "y": y}
                    ))
                )

    def on_button_click(self, event: Event, target: Button):
        if GameStore.player_turn_name == PlayerStore.name and self.is_hit_board:
            x, y = target.metaData["x"], target.metaData['y']
            if GameStore.player_hit[y][x] is None:
                Connection.send_request("game", "move", {
                    "playerName": PlayerStore.name,
                    "gameName": GameStore.name,
                    "cords": (x, y)
                })

                result = Connection.send_request(Config.GAME_CONTROLLER, "get-game-data",
                                                 {"gameName": GameStore.name, "playerName": PlayerStore.name})

                GameStore.set_game_data(result)

    def render(self, window):
        self.buttons.clear()
        self.add_buttons()
        for row in self.buttons:
            for button in row:
                button.render(window)
