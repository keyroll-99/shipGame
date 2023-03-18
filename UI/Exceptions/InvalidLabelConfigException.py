from UI.Models.LabelConfig import LabelConfig
from UI.Exceptions.InvalidUiConfigException import InvalidUiConfigException


class InvalidLabelConfigException(Exception):
    def __init__(self):
        super().__init__("Invalid Label config")

    @staticmethod
    def throw_if_invalid(config: LabelConfig):
        InvalidUiConfigException.throw_if_invalid(config)
        if config.text.strip() == "" or len(list(filter(lambda x: 0 <= x <= 255, config.color))) != 3:
            raise InvalidLabelConfigException
