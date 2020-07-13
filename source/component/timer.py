import pygame as pg
from .. import constants as c
import time


class Timer:
    def __init__(self,screen,state):

        self.screen = screen
        self.smallText = pg.font.SysFont("monospace", c.FONT_SIZE//4)
        self.seconds = 00
        self.minutes = 00
        self.hours   = 00
        self.aux = 1
        self.mainloop = state

    def break_loop(self):
        self.mainloop = False

    def count(self):
        begin = time.time()
        while self.mainloop:
            end =  time.time()
            self.seconds = end - begin
            if int(self.seconds) == 60:
                self.seconds = 00
                self.minutes += 1
                begin = time.time()
            if self.minutes == 60:
                self.minutes = 00
                self.hours += 1
                begin = time.time()
            
            output = self.smallText.render("Tiempo: " + str(self.hours)+":"+str(self.minutes)+":"+str(int(self.seconds)),0,c.BLACK)
            self.screen.blit(output,c.TIME_POS)
            pg.display.update()
            

            
            
            
            
             


