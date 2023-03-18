import pygame
from pygame import Surface, SurfaceType
from pygame.font import Font, SysFont
from pygame.event import Event
from pygame import mouse

from Models.GameObject import GameObject
from UI.Exceptions.InvalidButtonConfigException import InvalidButtonConfigException
from UI.Models.ButtonConfig import ButtonConfig


class Button(GameObject):
    backgroundColor: tuple[int, int, int]
    color: tuple[int, int, int]
    text: str
    font: Font
    buttonSurface: Surface

    def __init__(self, config: ButtonConfig):
        InvalidButtonConfigException.throw_if_invalid(config)
        super().__init__(config)
        self.text = config.text
        self.color = config.color
        self.font = SysFont('Comic Sans MS', config.fontSize)
        self.buttonSurface = Surface((config.width, config.height))
        self.buttonSurface.fill(config.backgroundColor)

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
        print("clicked")
        print(f"{event.type}")
        print(f"{mouse.get_pos()}")
        print(f"{mouse.get_pressed()}")

    def on_mouse_button_down(self, event: Event):
        print("mouse down")


