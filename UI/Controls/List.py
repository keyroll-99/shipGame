import math

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
    selectedIndex = None

    def __init__(self, config: ListConfig):
        InvalidListConfigException.throw_if_invalid(config)
        super().__init__(config)
        self.config = config
        self.font = SysFont(GlobalConfig.DEFAULT_FONT, config.fontSize)
        self.surface = Surface((config.width, config.height))
        self.surface.fill(config.backgroundColor)
        self.elementHeight = config.fontSize + 15
        self.eventsReaction = {
            pygame.MOUSEBUTTONDOWN: self.on_click
        }

    def render(self, window: Surface):
        top = 0
        self.surface.fill(self.config.backgroundColor)
        for index, element in enumerate(self.config.elements):
            if self.selectedIndex is None or self.selectedIndex != index:
                pygame.draw.rect(self.surface, Config.BACK_COLOR, (0, top, self.config.width, self.elementHeight), 1)
            else:
                pygame.draw.rect(self.surface, self.config.onClickColor, (0, top, self.config.width, self.elementHeight),
                                 0)
            text = self.font.render(element, False, self.config.color)
            self.surface.blit(text, [self.config.width / 2 - text.get_width() / 2, top])
            top += self.elementHeight

        window.blit(self.surface, (self.position.left, self.position.top))

    def on_click(self, e):
        if not self.is_mouse_over():
            return
        mouse_pos = pygame.mouse.get_pos()
        witch_element = math.floor((mouse_pos[1] - self.config.top) / self.elementHeight)
        if witch_element <= len(self.config.elements):
            self.selectedIndex = witch_element

    def get_selected(self):
        try:
            return self.config.elements[self.selectedIndex]
        except:
            return None
