from Config import Config
from Models.GameObject import GameObject
from Models.Position import Position
from UI.Controls.Button import Button, ButtonConfig
from UI.Controls.Input import Input, InputConfig
from UI.Controls.Label import Label, LabelConfig
import pygame


class ActionButtons(GameObject):
    createServerButton: Button
    joinToServerButton: Button
    serverNameInput: Input
    serverNameLabel: Label
    errorNameLabel: Label
    showError = False

    def __init__(self):
        super().__init__()
        self.__render_join_to_server()
        self.__render_create_server()

        self.eventsReaction = {
            **self.serverNameInput.eventsReaction,
            pygame.MOUSEBUTTONDOWN: self.on_mouse_button_down,
            pygame.MOUSEBUTTONUP: self.on_mouse_button_up
        }

    @staticmethod
    def on_create_server_click(e):
        print("create")

    @staticmethod
    def on_join_to_server_click(e):
        print('join')

    def on_mouse_button_down(self, e):
        if self.createServerButton.is_mouse_over():
            self.createServerButton.on_mouse_button_down(e)

        if self.joinToServerButton.is_mouse_over():
            self.joinToServerButton.on_mouse_button_down(e)

    def on_mouse_button_up(self, e):
        self.joinToServerButton.on_mouse_button_up(e)
        self.createServerButton.on_mouse_button_up(e)

    def render(self, window):
        self.createServerButton.render(window)
        self.joinToServerButton.render(window)
        self.serverNameLabel.render(window)
        self.serverNameInput.render(window)

    def __render_join_to_server(self):
        self.joinToServerButton = Button(ButtonConfig(
            "Join to server",
            Config.BACK_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Config.LIGHT_GREY_COLOR,
            Position(
                400,
                40,
                590,
                (Config.SCREEN_SIZE[1] / 2) - 200
            ),
            self.on_join_to_server_click
        ))

    def __render_create_server(self):
        self.serverNameLabel = Label(LabelConfig(
            "Server name: ",
            Config.BACK_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Position(
                250,
                40,
                (Config.SCREEN_SIZE[0] / 2) + 235,
                (Config.SCREEN_SIZE[1] / 2) - 250
            )
        ))

        self.serverNameInput = Input(InputConfig(
            Config.BACK_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Config.LIGHT_GREY_COLOR,
            Position(
                250,
                40,
                (Config.SCREEN_SIZE[0] / 2) + 240,
                (Config.SCREEN_SIZE[1] / 2) - 50
            )
        ))

        self.createServerButton = Button(ButtonConfig(
            "Create a server",
            Config.BACK_COLOR,
            Config.DEFAULT_FONT_SIZE,
            Config.GRASS_GREY,
            Position(
                400,
                40,
                (Config.SCREEN_SIZE[0] / 2) + 300,
                (Config.SCREEN_SIZE[1] / 2) - 200
            ),
            self.on_create_server_click
        ))
