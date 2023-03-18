import pygame.display

from Config import Config
from EventManager import EventManager
from Models.Position import Position
from ObjectManager import ObjectManager
from UI.Controls.Button import Button
from UI.Controls.Label import Label
from UI.Models.ButtonConfig import ButtonConfig
from UI.Models.LabelConfig import LabelConfig


class Game:
    window = None
    clock = None

    def __init__(self):
        self.__load_game()

    def main_loop(self):
        is_running = True

        while is_running:
            if EventManager.get_event(pygame.QUIT) is not None:
                is_running = False

            self.window.fill((255, 255, 255))

            EventManager.event_handle()
            ObjectManager.render_game_objects(self.window)

            pygame.display.update()

    def __load_game(self):
        pygame.init()
        self.window = pygame.display.set_mode(Config.SCREEN_SIZE)
        pygame.display.set_caption(Config.GAME_NAME)
        self.clock = pygame.time.Clock()
        ObjectManager.register_object(Label(LabelConfig("test", (0, 0, 0), 30, Position(200, 10, 100, 200))))
        ObjectManager.register_object(
            Button(ButtonConfig("test", (0, 0, 0), 30, (255, 50, 50), Position(200, 100, 0, 0))))
