
import pygame as pg
from . import constants as c


class Control():
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.gameExit = False
        self.clock = pg.time.Clock()
        self.fps = 60

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.gameExit = True

    def title_game(self):
        #Title
        self.myfont1 = pg.font.SysFont("monospace", c.FONT_SIZE)
        self.label_title = self.myfont1.render("BATTLE", 1, c.LIGHTYELLOW)
        SCREEN.blit(self.label_title, (c.SCREEN_WIDTH*0.35, c.SCREEN_HEIGHT*0.05))
        #Subtitle
        self.myfont2 = pg.font.SysFont("monospace", c.FONT_SIZE//2)
        self.label_subtitle = self.myfont2.render("Avatars vs Rooks", 1, c.LIGHTYELLOW)
        SCREEN.blit(self.label_subtitle, (c.SCREEN_WIDTH*0.30, c.SCREEN_HEIGHT*0.15))

    def main(self):
        while not self.gameExit:  
            self.event_loop()
            SCREEN.fill(c.SKY_BLUE)   #<---Intentar hacer todo esto en una funcion y 
            self.title_game()
            pg.display.update()       #  ver todavia mejor si se puede hacer desde archivos diferentes
            self.clock.tick(self.fps)


pg.init()
pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)