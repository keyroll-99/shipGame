from EventQueue.Events.ChangeViewEvent import ChangeViewEvent
from EventQueue.EventsProcessing.BaseEventProcessing import BaseEventProcessing
from View.ViewManager import ViewManager


class ChangeViewEventProcessing(BaseEventProcessing):

    def __init__(self):
        self.eventsReaction = {
            ChangeViewEvent.name: self.action
        }

    @staticmethod
    def action(data: ChangeViewEvent.data):
        ViewManager.load_view(data)
