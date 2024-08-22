import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen,'white', self.position, self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(angle)
        vector_2 = self.velocity.rotate(-angle)
        new_radius  = self.radius - ASTEROID_MIN_RADIUS
        new_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_1.velocity = vector_1
        new_2.velocity = vector_2
        new_1.velocity *= 1.2
        new_2.velocity *= 1.2