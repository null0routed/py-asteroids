import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    (pygame_init_mod, pygame_fail_mod) = pygame.init()
    print(f"Init: {pygame_init_mod}\nFailed: {pygame_fail_mod}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # player.add(updatables, drawables)
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatables.update(dt)
        for obj in drawables:
            obj.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
