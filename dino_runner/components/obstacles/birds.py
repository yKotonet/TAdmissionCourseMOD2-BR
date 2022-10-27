from dino_runner.components.obstacles.obstacles import Obstacle


class Birds(Obstacle):
    def __init__(self, image):
        self.step_index = 0
        self.type = 0
        self.image = image
        super().__init__(image, self.type, True)
        self.rect.y = 270
