import pygame as pg
from .. import constants as c
import time


class Timer:
    def __init__(self,screen,state):

        self.screen = screen
        self.smallText = pg.font.SysFont("monospace", c.FONT_SIZE_TIMER)
        self.seconds = 00
        self.minutes = 00
        self.hours   = 00
        self.aux = 1
        self.loop = state

    def break_loop(self):
        self.loop = False

    def count(self,begin):
        self.begin   = begin
        self.end     = time.time()
        self.seconds = self.end - self.begin   
        
        out = [self.seconds]  
        return out  
        
            
        
        
            
            
            
             


