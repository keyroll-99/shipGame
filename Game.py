import pygame.display

from Config import Config
from EventManager import EventManager
from EventQueue.EventsProcessing.CloseWindowEventProcessing import CloseWindowEventProcessing
from ObjectManager import ObjectManager
from View.ViewManager import ViewManager
from View import ViewNames
from Clock.GameClock import GameClock


class Game:
    window = None
    clock = None

    def __init__(self):
        self.__load_game()

    def main_loop(self):
        is_running = True

        while is_running:
            self.clock.update()
            EventManager.event_handle()

            if CloseWindowEventProcessing.is_window_close():
                is_running = False

            self.window.fill(Config.WHITE_COLOR)

            ObjectManager.render_game_objects(self.window)

            pygame.display.update()

    def __load_game(self):
        self.window = pygame.display.set_mode(Config.SCREEN_SIZE)
        pygame.display.set_caption(Config.GAME_NAME)
        self.clock = GameClock()
        ViewManager.init()
        ViewManager.load_view(ViewNames.MAIN_MENU)
