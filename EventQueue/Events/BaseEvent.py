class BaseEvent:
    name: str = ""
    data = None

    def __init__(self, data=None):
        self.data = data
