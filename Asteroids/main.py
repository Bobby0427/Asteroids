import pygame
from player import Player
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
def main():
    pygame.init()
    print(f"Starting Asteroidswith pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip() 
        dt = clock.tick(60) /1000
        
if __name__ == "__main__":
    main()
