import pygame as pg
from . import constants as c
import os

class Credit:
    
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.brandon =  pg.image.load(os.path.join(c.PATH,"Fotos","Brandon01.png"))
        self.juan =  pg.image.load(os.path.join(c.PATH,"Fotos","Juan01.png"))
        self.gameExit = False
        self.clock = pg.time.Clock()
        self.fps = 30

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.gameExit = True

    def text(self):
        #University
        self.myfont1 = pg.font.SysFont("monospace", 16)
        self.label_title = self.myfont1.render("Instituto Tecnologico de Costa Rica", 1, c.LIGHTYELLOW)
        self.screen.blit(self.label_title, (225,40))
        #Subtitle
        self.myfont2 = pg.font.SysFont("monospace", 16)
        self.label_subtitle = self.myfont2.render("Cartago, Costa Rica", 1, c.LIGHTYELLOW)
        self.screen.blit(self.label_subtitle, (300,70))
        #Title
        self.myfont3 = pg.font.SysFont("monospace", 16)
        self.label_title = self.myfont3.render("Version 1.0", 1, c.LIGHTYELLOW)
        self.screen.blit(self.label_title, (335,100))
        #Subtitle
        self.myfont4 = pg.font.SysFont("monospace", 16)
        self.label_subtitle = self.myfont4.render("Brandon Cortés Vargas", 1, c.LIGHTYELLOW)
        self.screen.blit(self.label_subtitle, (35,400))
        #Title
        self.myfont5 = pg.font.SysFont("monospace", 16)
        self.label_title = self.myfont5.render("Edad: 19", 1, c.LIGHTYELLOW)
        self.screen.blit(self.label_title, (35,420))
        #Subtitle
        self.myfont6 = pg.font.SysFont("monospace", 16)
        self.label_subtitle = self.myfont6.render("Carnet: 2020163216", 1, c.LIGHTYELLOW)
        self.screen.blit(self.label_subtitle, (35,440))
        #Title
        self.myfont7 = pg.font.SysFont("monospace", 16)
        self.label_title = self.myfont7.render("Juan Daniel Rodríguez Montero", 1, c.LIGHTYELLOW)
        self.screen.blit(self.label_title, (500,400))
        #Subtitle
        self.myfont8 = pg.font.SysFont("monospace", 16)
        self.label_subtitle = self.myfont8.render("Edad: 20", 1, c.LIGHTYELLOW)
        self.screen.blit(self.label_subtitle, (500,420))
        #Title
        self.myfont9 = pg.font.SysFont("monospace", 16)
        self.label_title = self.myfont9.render("Carnet: 2020426163", 1, c.LIGHTYELLOW)
        self.screen.blit(self.label_title, (500,440))
        

    def main(self):
        
        while not self.gameExit:
             
            self.event_loop() #captura eventos
            pg.display.update()
            GAME_SCREEN.fill(c.FONT_GREEN)   #color del fondo 
            self.screen.blit(self.brandon,(35,25))
            self.screen.blit(self.juan,(580,25))
            self.text()
            
            self.clock.tick(self.fps)
               

            


pg.init()
pg.display.set_caption(c.ORIGINAL_CAPTION)
GAME_SCREEN = pg.display.set_mode(c.SCREEN_SIZE)

