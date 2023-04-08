from EventQueue.Events.BaseEvent import BaseEvent


class CloseGameEvent(BaseEvent):
    name = "CloseGame"

    def __init__(self):
        super().__init__(None)
