import pygame as pg
from . import constants as c
import os

class Help:
    
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.font_help =  pg.image.load(os.path.join(c.PATH,"background","Fondo03.png"))
        
        self.gameExit = False
        self.clock = pg.time.Clock()
        self.fps = 30

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.gameExit = True

    def main(self):
        
        while not self.gameExit:
             
            self.event_loop() #captura eventos
            pg.display.update()
            GAME_SCREEN.fill(c.FONT_GREEN)   #color del fondo 
            self.screen.blit(self.font_help,(0,0))
            self.clock.tick(self.fps)
               
pg.init()
pg.display.set_caption(c.ORIGINAL_CAPTION)
GAME_SCREEN = pg.display.set_mode(c.SCREEN_SIZE)