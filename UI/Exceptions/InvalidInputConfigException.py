from UI.Models.InputConfig import InputConfig
from UI.Exceptions.InvalidUiConfigException import InvalidUiConfigException


class InvalidInputConfigException(Exception):
    def __init__(self):
        super().__init__("Input invalid config")

    @staticmethod
    def throw_if_invalid_config(config: InputConfig):
        InvalidUiConfigException.throw_if_invalid(config)
        if len(list(filter(lambda x: 0 <= x <= 255, config.color))) != 3:
            raise InvalidInputConfigException
