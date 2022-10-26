import pygame
from random import randint
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.step_index = 0

    def update(self, game):

        if self.step_index > 10:
            self.step_index = 0
        if len(self.obstacles) == 0:

            orandom = randint(0, 1)
            cactusSmallLarge = [SMALL_CACTUS, LARGE_CACTUS]
            cactus_Random = cactusSmallLarge[orandom]
            cactus = Cactus(cactus_Random)

            if orandom == 1:
                cactus = Cactus(cactus_Random, 300)

            self.obstacles.append(cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
