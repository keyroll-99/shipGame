from UI.Models.ListConfig import ListConfig
from UI.Exceptions.InvalidUiConfigException import InvalidUiConfigException


class InvalidListConfigException(Exception):
    def __init__(self):
        super().__init__("Invalid Label config")

    @staticmethod
    def throw_if_invalid(config: ListConfig):
        InvalidUiConfigException.throw_if_invalid(config)
