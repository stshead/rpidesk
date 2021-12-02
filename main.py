import time
import numpy as np
from rpievdev import TDEV
import pygame
import pygame.gfxdraw

def main():
    ## Touch screen input
    #ts = TDEV()

    ## pygame setup
    clock = pygame.time.Clock()
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)

    ## test
    #screen.fill((0, 150, 0))
    BG = pygame.image.load('img/bg.bmp')
    WCOL = pygame.image.load('img/wcol.bmp')
    ball = pygame.image.load('img/ball.bmp')
    screen.blit(BG,(0, 0))
    pygame.display.flip()

    time.sleep(1)

    fps = 58
    ang = np.linspace(0,2*np.pi,2*fps)
    x = [int(np.round(400+50*np.sin(a))) for a in ang]
    y = [int(np.round(240+50*np.cos(a))) for a in ang]
    
    if True:
        for j in range(10):
            for i in range(len(x)):
                screen.blit(BG,(0, 0))
                screen.blit(ball,(x[i], y[i]))
                pygame.display.flip()
                dt = clock.tick(fps)

    if False:
        for j in range(50):
            for i in range(6):
                screen.blit(BG,(0, 0))
                screen.blit(WCOL,(i*10, 0))
                pygame.display.flip()
                dt = clock.tick(fps)

    print("sleeping...")

    time.sleep(1)
    print("ok")


if __name__ == "__main__":
    main()
