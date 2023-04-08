import pygame

from Config import Config
from Connection.Connection import Connection
from EventQueue.Events.CloseGameEvent import CloseGameEvent
from EventQueue.EventsProcessing.BaseEventProcessing import BaseEventProcessing
from Store.PlayerStore import PlayerStore


class CloseWindowEventProcessing(BaseEventProcessing):
    __windowsIsClose = False

    def __init__(self):
        self.eventsReaction = {
            pygame.QUIT: CloseWindowEventProcessing.close_window,
            CloseGameEvent.name: CloseWindowEventProcessing.close_game
        }

    @staticmethod
    def close_window():
        CloseWindowEventProcessing.__disconnect_from_server()
        CloseWindowEventProcessing.__windowsIsClose = True

    @staticmethod
    def close_game(data):
        CloseWindowEventProcessing.__disconnect_from_server()
        CloseWindowEventProcessing.__windowsIsClose = True

    @staticmethod
    def __disconnect_from_server():
        if PlayerStore.name != "":
            Connection.send_request(Config.PLAYER_CONTROLLER, "exit", PlayerStore.name)

    @staticmethod
    def is_window_close():
        return CloseWindowEventProcessing.__windowsIsClose
