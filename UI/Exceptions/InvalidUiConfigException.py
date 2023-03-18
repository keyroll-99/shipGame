from Models.Position import Position


class InvalidUiConfigException(Exception):
    def __init__(self):
        super().__init__("Invalid Ui Config")

    @staticmethod
    def throw_if_invalid(config: Position):
        if config.width <= 0 or config.height <= 0 or config.top < 0 or config.left < 0:
            raise InvalidUiConfigException
