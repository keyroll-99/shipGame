from UI.Models.LabelConfig import LabelConfig
from UI.Exceptions.InvalidLabelConfig import InvalidLabelConfig
from UI.Controls._UiItem import UiItem
from pygame import Surface, SurfaceType
from pygame.font import Font, SysFont


class Label(UiItem):
    color: tuple[int, int, int]
    text: str
    font: Font

    def __init__(self, config: LabelConfig):
        InvalidLabelConfig.throw_if_invalid(config)
        super().__init__(config)
        self.text = config.text
        self.color = config.color
        self.font = SysFont('Comic Sans MS', config.fontSize)

    def render(self, window: Surface | SurfaceType):
        text_surface = self.font.render(self.text, False, self.color)
        window.blit(text_surface, (self.position.left, self.position.top))
