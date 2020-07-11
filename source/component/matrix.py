import pygame as pg
from .. import constants as c
class Board:
    def __init__(self,screen):
        self.color = 0
        self.screen = screen

    def create_board(self):
        for i in range(c.M_WIDTH):
            for j in range(c.M_HEIGHT):
                x,y = i*c.DIMENTION,j*c.DIMENTION
                pg.draw.rect(self.screen,c.BLACK,[x+237.5,y+10.5,c.DIMENTION,c.DIMENTION],0)
