import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20, 50)
        pos_vec = self.velocity.rotate(rand_angle)
        neg_vec = self.velocity.rotate(-rand_angle)

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        pos_asteroid = Asteroid(self.position.x, self.position.y, new_rad)
        neg_asteroid = Asteroid(self.position.x, self.position.y, new_rad)
        pos_asteroid.velocity = pos_vec * 1.2
        neg_asteroid.velocity = neg_vec * 1.2
