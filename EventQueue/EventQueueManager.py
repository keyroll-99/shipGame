from EventQueue.Events.BaseEvent import BaseEvent


class EventQueueManager:
    __events: list[BaseEvent] = []

    @staticmethod
    def publish_event(event: BaseEvent):
        EventQueueManager.__events.append(event)

    @staticmethod
    def get_events():
        events = EventQueueManager.__events.copy()
        EventQueueManager.__events.clear()
        return events
