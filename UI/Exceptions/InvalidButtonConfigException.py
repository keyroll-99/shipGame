from UI.Exceptions.InvalidUiConfigException import InvalidUiConfigException
from UI.Models.ButtonConfig import ButtonConfig


class InvalidButtonConfigException(Exception):
    def __init__(self):
        super().__init__("Invalid Label config")

    @staticmethod
    def throw_if_invalid(config: ButtonConfig):
        InvalidUiConfigException.throw_if_invalid(config)
        if len(list(filter(lambda x: 0 <= x <= 255, config.color))) != 3 or len(
                list(filter(lambda x: 0 <= x <= 255, config.backgroundColor))) != 3:
            raise InvalidButtonConfigException
