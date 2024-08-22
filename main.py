import pygame
from constants import *
from player import Player

from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    game_running = True
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    clock =  pygame.time.Clock()
    dt = 0


    asteroid_field = AsteroidField()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, shots_group=shots)
    Asteroid.containers = updateable, drawable, asteroids
    updateable.add(player, asteroid_field, shots)
    drawable.add(player, shots)




    while game_running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)

        for d in drawable:
            d.draw(screen)
        for u in updateable:
            u.update(dt)
        for a in asteroids:
            collision = a.check_collisions(player)
            if collision == True:
                print("Game over!")
                game_running = False
            for s in shots:
                collision = s.check_collisions(a)
                if collision:
                    a.split()
                    s.kill()

        for shot in shots:
            shot.update(dt)
            shot.draw(screen)

        pygame.display.flip()
        clock_return = clock.tick(60)
        dt = float(clock_return) / 1000
    pygame.quit()


if __name__ == "__main__":
    main()
