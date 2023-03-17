from UI.Exceptions import InvalidUiConfigException


class UiPositionConfig:
    width = None
    height = None
    top = None
    left = None

    def __init__(self, width: int, height: int, top: int, left: int):
        self.width = width
        self.height = height
        self.left = left
        self.top = top

    @staticmethod
    def throw_if_invalid(config: "UiPositionConfig"):
        if config.width <= 0 or config.height <= 0 or config.top <= 0 or config.left <= 0:
            raise InvalidUiConfigException
