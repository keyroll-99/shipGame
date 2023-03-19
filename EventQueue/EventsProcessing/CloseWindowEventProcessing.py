import pygame

from EventQueue.EventsProcessing.BaseEventProcessing import BaseEventProcessing


class CloseWindowEventProcessing(BaseEventProcessing):
    __windowsIsClose = False

    def __init__(self):
        self.eventsReaction = {
            pygame.QUIT: CloseWindowEventProcessing.close_window
        }

    @staticmethod
    def close_window():
        CloseWindowEventProcessing.__windowsIsClose = True

    @staticmethod
    def is_window_close():
        return CloseWindowEventProcessing.__windowsIsClose
