import pygame

from Connection.Connection import Connection
from Config import Config
from Models.GameObject import GameObject
from Models.Position import Position
from UI.Controls.Button import Button, ButtonConfig
from UI.Controls.Input import Input, InputConfig
from UI.Controls.Label import Label, LabelConfig
from Store.PlayerStore import PlayerStore
from EventQueue.EventQueueManager import EventQueueManager
from EventQueue.Events.ChangeViewEvent import ChangeViewEvent
from View.ViewNames import GAME_LOBBY
from Store.GameStore import GameStore


class ServerListAction(GameObject):
    createServerButton: Button
    joinToServerButton: Button
    serverNameInput: Input
    serverNameLabel: Label
    errorNameLabel: Label
    allGameObjects: list[GameObject] = []
    showError = False
    parent = None

    def __init__(self, parent):
        super().__init__()
        self.__render_join_to_server()
        self.__render_create_server()
        self.__render_error_label()

        self.eventsReaction = {
            pygame.MOUSEBUTTONDOWN: self.on_mouse_button_down,
            pygame.MOUSEBUTTONUP: self.on_mouse_button_up,
            pygame.KEYDOWN: self.on_key_down,
        }
        self.parent = parent

    def on_create_server_click(self, e):
        server_name = self.serverNameInput.text

        if server_name == "":
            self.errorNameLabel.text = "Server name can't be empty"
            self.showError = True
            return
        player_name = PlayerStore.name
        response = Connection.send_request(Config.GAME_ROOM_CONTROLLER, "create",
                                           {"playerName": player_name, 'name': server_name})
        if not response["isSuccess"]:
            self.errorNameLabel.text = response["message"]
            self.showError = True
            return
        GameStore.name = server_name
        EventQueueManager.publish_event(ChangeViewEvent(GAME_LOBBY))

    def on_join_to_server_click(self, e):
        selected_server = self.parent.gameList.serverList.get_selected()
        player_name = PlayerStore.name;
        response = Connection.send_request(Config.GAME_CONTROLLER, "join",
                                           {"playerName": player_name, "gameName": selected_server})

        if not response['isSuccess']:
            self.errorNameLabel.text = response['message']
            self.showError = True

        GameStore.name = selected_server
        EventQueueManager.publish_event(ChangeViewEvent(GAME_LOBBY))

    def on_mouse_button_down(self, e):
        for gameObject in self.allGameObjects:
            if pygame.MOUSEBUTTONDOWN in gameObject.eventsReaction.keys():
                gameObject.eventsReaction[pygame.MOUSEBUTTONDOWN](e)

    def on_mouse_button_up(self, e):
        for gameObject in self.allGameObjects:
            if pygame.MOUSEBUTTONUP in gameObject.eventsReaction.keys():
                gameObject.eventsReaction[pygame.MOUSEBUTTONUP](e)

    def on_key_down(self, e):
        for gameObject in self.allGameObjects:
            if pygame.KEYDOWN in gameObject.eventsReaction.keys():
                gameObject.eventsReaction[pygame.KEYDOWN](e)

    def render(self, window):
        self.createServerButton.render(window)
        self.joinToServerButton.render(window)
        self.serverNameLabel.render(window)
        self.serverNameInput.render(window)
        if self.showError:
            self.errorNameLabel.render(window)

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
        self.allGameObjects.append(self.joinToServerButton)

    def __render_error_label(self):
        self.errorNameLabel = Label(LabelConfig(
            "Server with this name exists",
            Config.RED_COLOR,
            20,
            Position(
                250,
                40,
                (Config.SCREEN_SIZE[0] / 2) + 275,
                (Config.SCREEN_SIZE[1] / 2) - 150
            )
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

        self.allGameObjects.append(self.serverNameLabel)

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

        self.allGameObjects.append(self.serverNameInput)

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
        self.allGameObjects.append(self.createServerButton)
