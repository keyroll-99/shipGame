from UI.Models.LabelConfig import LabelConfig
from UI.Exceptions.InvalidLabelConfigException import InvalidLabelConfigException
from Models.GameObject import GameObject
from pygame import Surface, SurfaceType
from pygame.font import Font, SysFont
from Config import Config as GlobalConfig

class Label(GameObject):
    color: tuple[int, int, int]
    text: str
    font: Font

    def __init__(self, config: LabelConfig):
        InvalidLabelConfigException.throw_if_invalid(config)
        super().__init__(config)
        self.text = config.text
        self.color = config.color
        self.font = SysFont(GlobalConfig.DEFAULT_FONT, config.fontSize)

    def render(self, window: Surface | SurfaceType):
        text_surface = self.font.render(self.text, False, self.color)
        window.blit(text_surface, (self.position.left, self.position.top))
