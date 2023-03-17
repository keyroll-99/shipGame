from UI.Models.UiPositionConfig import UiPositionConfig
from UI.Controls.UiItem import UiItem


class Label(UiItem):
    text = None

    def __init__(self, position: UiPositionConfig, text: str):
        super().__init__(position)
        self.text = text

    def render(self, screen, ):
        pass



