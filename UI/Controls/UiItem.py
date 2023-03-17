from UI.Models.UiPositionConfig import UiPositionConfig


class UiItem:
    position = None

    def __init__(self, position: UiPositionConfig):
        UiPositionConfig.throw_if_invalid(position)
        self.position = position

    def render(self, screen):
        raise NotImplemented("Not implemented")
