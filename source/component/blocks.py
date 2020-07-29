import pygame as pg
from .. import constants as c

class Block:
    def __init__(self,x,y,w,h):
        self.rect = (x,y,w,h)


    def draw_rect(self,screen):
        pg.draw.rect(screen,c.TRANS,self.rect,1)