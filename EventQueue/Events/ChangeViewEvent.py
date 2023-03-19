from EventQueue.Events.BaseEvent import BaseEvent


class ChangeViewEvent(BaseEvent):
    name = "ChangeView"
    data: str = ""

    def __init__(self, goToView: str):
        super().__init__(goToView)
