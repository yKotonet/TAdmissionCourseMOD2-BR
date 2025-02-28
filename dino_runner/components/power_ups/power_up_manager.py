from asyncio import shield
import random
import pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.slow import Slow


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

        self.randomization = random.randint(0, 1)
        self.power_upss = [Shield, Slow]
        self.power_ups_random = self.power_upss[self.randomization]

    def generate_power_up(self, score):

        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.power_ups.append(self.power_ups_random())

    def update(self, score, game_speed, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + \
                    (power_up.duration * 800)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
