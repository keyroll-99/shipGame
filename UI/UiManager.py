from pygame import Surface, SurfaceType
from UI.Controls.Label import Label
from UI.Models.LabelConfig import LabelConfig
from Models.Position import Position

from UI.Controls._UiItem import UiItem


class UiManager:
    window: Surface | SurfaceType
    uiElements: list[UiItem] = []

    def __init__(self, window: Surface | SurfaceType):
        self.window = window
        self.uiElements.append(Label(LabelConfig("test", (0, 0, 0), 30, Position(200, 10, 100, 200))))

    def render_ui(self):
        for uiElement in self.uiElements:
            uiElement.render(self.window)
