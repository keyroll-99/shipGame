class InvalidUiConfigException(Exception):
    def __init__(self):
        super().__init__("Invalid Ui Config")
