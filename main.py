# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Hello from asteroids!")
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            else:
                dt = clock.tick(60)/1000
        screen.fill("black")
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
