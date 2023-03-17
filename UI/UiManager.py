import pygame.font
from pygame import Surface, SurfaceType
from pygame.font import Font
from UI.Controls.UiItem import UiItem


class UiManager:
    window: Surface | SurfaceType
    font: Font
    uiElements: list[UiItem] = []

    def __init__(self, window: Surface | SurfaceType):
        self.window = window
        self.font = pygame.font.SysFont('Comic Sans MS', 30)


    def render_ui(self):
        for uiElement in self.uiElements:
            pass