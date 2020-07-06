
import pygame as pg
from . import constants as c


class Control():
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.crashed = False
        self.clock = pg.time.Clock()
        self.fps = 60

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.crashed = True
    def main(self):
        while not self.crashed:  
            self.event_loop()
            pg.display.update()
            self.clock.tick(self.fps)


pg.init()
pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)