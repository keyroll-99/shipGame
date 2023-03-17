import pygame.display
from Config import Config
from UI.UiManager import UiManager

class Game:
    window = None
    clock = None
    uiManager: UiManager

    def __init__(self):
        self.__load_game()
        self.uiManager = UiManager(self.window)

    def main_loop(self):
        is_running = True

        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

            for uiElement in self.uiObject:
                uiElement.render(pygame.display)

            pygame.display.update()

    def __load_game(self):
        pygame.init()
        self.window = pygame.display.set_mode(Config.SCREEN_SIZE)
        pygame.display.set_caption(Config.GAME_NAME)
        self.clock = pygame.time.Clock()
