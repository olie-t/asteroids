import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    clock =  pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)
        pygame.display.flip()
        clock_return = clock.tick(60)
        dt = float(clock_return) / 1000


if __name__ == "__main__":
    main()
