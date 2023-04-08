import pygame
from pygame import Surface
from pygame.event import Event, EventType
from pygame.font import Font, SysFont

from Config import Config as GlobalConfig
from Models.GameObject import GameObject
from UI.Models.InputConfig import InputConfig
from UI.Exceptions.InvalidInputConfigException import InvalidUiConfigException
from Clock.GameClock import GameClock


class Input(GameObject):
    text: str = ""
    isFocused: bool = False
    backgroundColor: tuple[int, int, int]
    color: tuple[int, int, int]
    font: Font
    inputSurface: Surface
    isCurrentPointShow: bool = False
    timeDelayBetweenCurrentPointToggle = 1
    currentDelayBetweenPointToggle = 0

    def __init__(self, config: InputConfig):
        InvalidUiConfigException.throw_if_invalid(config)
        super().__init__(config)

        self.backgroundColor = config.backgroundColor
        self.color = config.color
        self.font = SysFont(GlobalConfig.DEFAULT_FONT, config.fontSize)
        self.inputSurface = Surface((config.width, config.height))
        self.inputSurface.fill(config.backgroundColor)

        self.eventsReaction = {
            pygame.MOUSEBUTTONDOWN: self.on_focus,
            pygame.KEYDOWN: self.on_key_dow
        }

    def render(self, window: Surface):
        text_surface = self.font.render(self.__get_text_to_print(), False, self.color)
        self.inputSurface.fill(self.backgroundColor)
        self.inputSurface.blit(text_surface, [self.position.width / 2 - text_surface.get_width() / 2,
                                              self.position.height / 2 - text_surface.get_height() / 2])
        window.blit(self.inputSurface, (self.position.left, self.position.top))

    def on_focus(self, event: Event | EventType):
        self.isFocused = self.is_mouse_over()

    def on_key_dow(self, event: Event):
        if self.isFocused:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def __get_text_to_print(self) -> str:
        text = self.text
        self.currentDelayBetweenPointToggle += GameClock.dt

        if self.isFocused:
            if not self.isCurrentPointShow:
                text += "|"
            if self.currentDelayBetweenPointToggle > self.timeDelayBetweenCurrentPointToggle:
                self.isCurrentPointShow = not self.isCurrentPointShow
                self.currentDelayBetweenPointToggle = 0

        return text
