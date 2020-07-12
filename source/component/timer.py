import pygame as pg
from .. import constants as c
import time

class Timer:
    def __init__(self):
        self.start_ticks = pg.time.get_ticks() #starter tick
        self.mainloop = True
        self.seconds = 00
        self.minutes = 00
        self.hours   = 00
    def count(self):
        while self.mainloop: # mainloop
            time.sleep(1)
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 00
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 00
                self.hours += 1
            print("Tiempo: " + str(self.hours)+":"+str(self.minutes)+":"+str(self.seconds))
