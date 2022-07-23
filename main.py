import time
import numpy as np
from rpievdev import TDEV
import pygame
import pygame.gfxdraw
import importlib
import page0
import page1
import page2
import page3
import page4

def main():
    ## Touch screen input
    ts = TDEV()

    ## constants
    FPS = 58

    ## pygame setup
    clock = pygame.time.Clock()
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)

    ## load images
    bye = pygame.image.load('img/bye.bmp')

    ## load pages
    pages = []
    pages.append(page0.PAGE())
    pages.append(page1.PAGE())
    pages.append(page2.PAGE())
    pages.append(page3.PAGE())
    pages.append(page4.PAGE())

    ## variables
    page=0

    ## main loop
    while(ts.activearray[3]==0):
        page = pages[page].draw(screen,ts,page)
        dt = clock.tick(FPS)
        pygame.display.flip()

    ## exit 
    screen.blit(bye,(0, 0))
    pygame.display.flip()
    ts.abort=True
    ts.thread.join()
    time.sleep(2)
    print("ok")
    return

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
    
    pp = page0.PAGE()
    pp.test()

    if True:
        for j in range(3):
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

    importlib.reload(page0)
    pp = page0.PAGE()
    pp.test()    

    ts.abort=True
    print("Touch device to exit...")
    ts.thread.join()

    print("ok")


if __name__ == "__main__":
    main()
