from pygame.time import Clock
from Config import Config


class GameClock:
    dt: float
    clock: Clock

    def __init__(self):
        self.clock = Clock()

    def update(self):
        GameClock.dt = self.clock.tick(Config.MAX_FPS) / 1000.0
