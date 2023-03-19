from typing import Callable

import pygame
from pygame import Surface, SurfaceType
from pygame.event import Event
from pygame.font import Font, SysFont

from Models.GameObject import GameObject
from UI.Exceptions.InvalidButtonConfigException import InvalidButtonConfigException
from UI.Models.ButtonConfig import ButtonConfig
from ObjectManager import ObjectManager


class Button(GameObject):
    backgroundColor: tuple[int, int, int]
    color: tuple[int, int, int]
    text: str
    font: Font
    buttonSurface: Surface
    onClick: Callable[[Event], None]
    isClicked = False

    def __init__(self, config: ButtonConfig):
        InvalidButtonConfigException.throw_if_invalid(config)
        super().__init__(config)
        self.text = config.text
        self.color = config.color
        self.font = SysFont('Comic Sans MS', config.fontSize)
        self.buttonSurface = Surface((config.width, config.height))
        self.buttonSurface.fill(config.backgroundColor)
        self.onClick = config.onClick

        self.eventsReaction = {
            pygame.MOUSEBUTTONUP: self.on_mouse_button_up,
            pygame.MOUSEBUTTONDOWN: self.on_mouse_button_down
        }

    def render(self, window: Surface | SurfaceType):
        text_surface = self.font.render(self.text, False, self.color)
        self.buttonSurface.blit(text_surface, [self.position.width / 2 - text_surface.get_width() / 2,
                                               self.position.height / 2 - text_surface.get_height() / 2])
        window.blit(self.buttonSurface, (self.position.left, self.position.top))

    def on_mouse_button_up(self, event: Event):
        self.isClicked = False

    def on_mouse_button_down(self, event: Event):
        self.isClicked = True
        if self.onClick is None:
            raise NotImplemented("On click not implemented")
        self.onClick(event)


