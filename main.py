import pygame
import sys

# define things
## sizes??
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

## colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def main():
    pygame.init()

    ## SETUP
    framerate = 60
    FPS = pygame.time.Clock()

    pygame.display.set_caption("flappy_bird_test")

    # create a surface on screen that has the size of SCREEN_WIDTH x SCREEN_HEIGHT
    gameScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameScreen.fill(BLACK)

    running = True

    # main loop
    while running:

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pygame.quit()
                sys.exit()

        gameScreen.fill(BLACK)
        pygame.display.update()
        FPS.tick(framerate)

if __name__ == '__main__':
    main()
