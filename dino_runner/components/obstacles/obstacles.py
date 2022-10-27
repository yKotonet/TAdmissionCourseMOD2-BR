from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image, type, bird):
        self.step_index = 0
        self.image = image[self.type]
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.bird = bird
        self.image_bird = image

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        if self.bird:
            self.voa_Passaro()

    def voa_Passaro(self):

        if self.step_index >= 10:
            self.step_index = 0

        self.type = 0 if self.step_index < 5 else 1
        self.image = self.image_bird[self.type]
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
