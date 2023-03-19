class BaseEventProcessing:
    eventsReaction: dict

    @staticmethod
    def action(data):
        raise NotImplemented
