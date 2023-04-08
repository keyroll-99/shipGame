import pygame
from pygame import Surface
from pygame.font import Font, SysFont

from Config import Config
from Config import Config as GlobalConfig
from Models.GameObject import GameObject
from UI.Exceptions.InvalidListConfigException import InvalidListConfigException
from UI.Models.ListConfig import ListConfig


class List(GameObject):
    config: ListConfig
    font: Font
    surface = Surface

    def __init__(self, config: ListConfig):
        InvalidListConfigException.throw_if_invalid(config)
        super().__init__(config)
        self.config = config
        self.font = SysFont(GlobalConfig.DEFAULT_FONT, config.fontSize)
        self.surface = Surface((config.width, config.height))
        self.surface.fill(config.backgroundColor)

    def render(self, window: Surface):
        top = 0
        for element in self.config.elements:
            pygame.draw.rect(self.surface, Config.BACK_COLOR, (0, top, self.config.width, self.config.fontSize + 15), 1)
            text = self.font.render(element, False, self.config.color)
            self.surface.blit(text, [self.config.width / 2 - text.get_width() / 2, top])
            top += self.config.fontSize + 15

        window.blit(self.surface, (self.position.left, self.position.top))
