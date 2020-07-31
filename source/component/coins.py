import pygame as pg
import os
from .. import constants as c

class Coins():  #1
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.star_image = pg.image.load(os.path.join(c.PATH,"star","Coin01.png"))
        self.star_rect = self.star_image.get_rect()
        self.star_rect.centerx = x
        self.star_rect.centery = y

    def draw(self,screen):
        screen.blit(self.star_image,self.star_rect)