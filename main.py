# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Hello from asteroids!")
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    new_asteroidfield = AsteroidField()
    Shot.containers = (updatable, drawable, shots)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            else:
                updatable.update(dt)
                for asteroid in asteroids:
                    if asteroid.check_collision(player):
                        sys.exit("Game over!")
                screen.fill("black")
                for sprite in drawable:
                    sprite.draw(screen)
                pygame.display.flip()
                dt = clock.tick(60)/1000
        
if __name__ == "__main__":
    main()
