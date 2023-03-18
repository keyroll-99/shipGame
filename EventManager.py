import pygame
from pygame.event import Event, get as get_all_events

from Models.GameObject import GameObject
from ObjectManager import ObjectManager


class EventManager:
    @staticmethod
    def get_event(eventType) -> Event | None:
        try:
            events = get_all_events()
            return list(filter(lambda x: x.type == eventType, events))[0]
        except IndexError:
            return None

    @staticmethod
    def event_handle():
        for event in get_all_events():
            game_objects = list(filter(lambda x: event.type in x.eventsReaction, ObjectManager.get_all_objects()))
            for game_object in game_objects:
                if EventManager.mouse_is_over_game_object(game_object):
                    game_object.eventsReaction[event.type](event)

    @staticmethod
    def mouse_is_over_game_object(gameObject: GameObject):
        mouse_position = pygame.mouse.get_pos()

        return gameObject.position.left < mouse_position[0] < gameObject.position.left + gameObject.position.width \
            and gameObject.position.top < mouse_position[1] < gameObject.position.top + gameObject.position.height
