import pygame
import pygame.gfxdraw
import time
import numpy as np

## page 1
class PAGE:
    def __init__(self):
        self.bg = pygame.image.load('img/bg.bmp')
        self.circlel = pygame.image.load('img/circlel.bmp')
        self.circler = pygame.image.load('img/circler.bmp')
        ## small rectangle area at the botton-right corner
        self.home = pygame.Rect(750,430,50,50)
        self.slidecolor = pygame.Color(18, 168, 124, a=255)
        self.spx = 200
        self.spy = 200
        self.tx = 0
        self.state = 0
        self.width = 0
        self.lastwidth = 0

    def draw(self, screen, ts, page):
        ## draw
        screen.blit(self.bg,(0,0))

        ## Loads screen brightness on first frame
        if self.state==0:
            self.width = 0
            self.tx = 0
            self.state = 1

        ## draw slider
        sliderect = pygame.Rect(self.spx+15, self.spy, self.width, 30)
        pygame.gfxdraw.box(screen, sliderect, self.slidecolor)
        screen.blit(self.circlel,(self.spx, self.spy))
        screen.blit(self.circler,(self.spx+15+self.width, self.spy))

        pygame.gfxdraw.box(screen, self.home, self.slidecolor)

        ## check for escape touch
        if ts.activearray[0]:
            ## exit if touch home area
            if self.home.collidepoint(ts.posx[0], ts.posy[0]):
                self.state=0
                page=0
            else:
                ## if touch lower screen, move slider
                if ts.posy[0]>self.spy:
                    if self.state == 1:
                        self.tx = ts.posx[0]
                        self.lastwidth = self.width
                        self.state = 2
                    else:
                        xdif = ts.posx[0]-self.tx
                        newwidth = self.lastwidth+xdif
                        if (newwidth>=0) and (newwidth<=200): 
                            self.width = newwidth
                else:
                    self.state=1

        return page