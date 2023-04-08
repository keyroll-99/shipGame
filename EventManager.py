import pygame
from pygame.event import Event, get as get_all_events

from EventQueue.EventsProcessing.BaseEventProcessing import BaseEventProcessing
from EventQueue.EventsProcessing.ChangeViewEventProcessing import ChangeViewEventProcessing
from EventQueue.EventsProcessing.CloseWindowEventProcessing import CloseWindowEventProcessing
from Models.GameObject import GameObject
from ObjectManager import ObjectManager
from EventQueue.EventQueueManager import EventQueueManager


class EventManager:
    eventProcessors: list[BaseEventProcessing] = [CloseWindowEventProcessing(), ChangeViewEventProcessing()]

    @staticmethod
    def get_event(eventType) -> Event | None:
        try:
            events = get_all_events()
            return list(filter(lambda x: x.type == eventType, events))[0]
        except IndexError:
            return None

    @staticmethod
    def event_handle():
        # it can be optimized
        all_custom_events = EventQueueManager.get_events()
        for custom_event in all_custom_events:
            game_objects = list(
                filter(lambda x: custom_event.name in x.eventsReaction, ObjectManager.get_all_objects()))

            for game_object in game_objects:
                game_object.eventsReaction[custom_event](custom_event.data)

            for event_processor in EventManager.eventProcessors:
                if custom_event.name in event_processor.eventsReaction:
                    event_processor.eventsReaction[custom_event.name](custom_event.data)

        for event in get_all_events():
            game_objects = list(filter(lambda x: event.type in x.eventsReaction, ObjectManager.get_all_objects()))

            for game_object in game_objects:
                game_object.eventsReaction[event.type](event)

            for event_processor in EventManager.eventProcessors:
                if event.type in event_processor.eventsReaction:
                    event_processor.eventsReaction[event.type]()
