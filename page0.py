import pygame
import pygame.gfxdraw
import time

## page 0
class PAGE:
    def __init__(self):
        self.bg = pygame.image.load('img/bg.bmp')
        self.blight = pygame.image.load('img/b_light.bmp')
        self.button = pygame.image.load('img/button.bmp')
        self.gapx = 64
        self.gapy = 80
    
    def draw(self, screen, ts, page):
        ## draw buttons
        screen.blit(self.bg,(0,0))
        b1r = screen.blit(self.blight,(self.gapx, self.gapy))
        b2r = screen.blit(self.button,(2*self.gapx+1*120,self.gapy))
        b3r = screen.blit(self.button,(3*self.gapx+2*120,self.gapy))
        b4r = screen.blit(self.button,(4*self.gapx+3*120,self.gapy))

        ## check for button touch
        if ts.activearray[0]:
            if b1r.collidepoint(ts.posx[0], ts.posy[0]):
                page=1
            elif b2r.collidepoint(ts.posx[0], ts.posy[0]):
                page=2
            elif b3r.collidepoint(ts.posx[0], ts.posy[0]):
                page=3
            elif b4r.collidepoint(ts.posx[0], ts.posy[0]):
                page=4

        return page