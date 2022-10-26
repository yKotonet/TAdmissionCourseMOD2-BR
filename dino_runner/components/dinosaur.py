import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

X_POS = 80
Y_POS = 310
Y_POS_DUCK = 340
JUMP_VEL = 8.5
DUCK_VEL = 8.5


class Dinosaur(Sprite):

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_jump = False
        self.dino_run = True
        self.jump_vel = JUMP_VEL
        self.dino_duck = False
        self.duck_vel = DUCK_VEL

    def update(self, user_input):
        if self.dino_jump:
            self.jump()

        if self.dino_duck:
            self.ducking()

        if self.dino_run:
            self.run()

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_DOWN] and not self.dino_duck and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True

        if user_input[pygame.K_UP] and not self.dino_jump and not self.dino_duck:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False

        if not self.dino_jump and not self.dino_duck:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def ducking(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        if self.dino_duck:
            self.dino_rect.y = 340
            self.dino_rect.x = X_POS
            self.duck_vel -= 10
        if self.duck_vel < -DUCK_VEL:
            self.dino_duck = False
            self.duck_vel = DUCK_VEL
        self.step_index += 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
