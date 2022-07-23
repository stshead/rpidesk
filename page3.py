import pygame
import pygame.gfxdraw
import time

## page 3
class PAGE:
    def __init__(self):
        self.bg = pygame.image.load('img/bg.bmp')
        ## small rectangle area at the botton-right corner
        self.home = pygame.Rect(750,430,50,50)

    def draw(self, screen, ts, page):
        ## draw buttons
        screen.blit(self.bg,(0,0))

        ## check for escape touch
        if ts.activearray[0]:
            if self.home.collidepoint(ts.posx[0], ts.posy[0]):
                page=0

        return page