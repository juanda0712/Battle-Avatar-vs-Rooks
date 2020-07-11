from . import constants as c
import pygame as pg
from .component import matrix


class GameScreen:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.gameExit = False
        self.clock = pg.time.Clock()
        self.fps = 60

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.gameExit = True

    def main(self):
        while not self.gameExit:  
            self.event_loop()
            GAME_SCREEN.fill(c.LIGHTYELLOW)  
            board.create_board() 
            pg.display.update()       
            self.clock.tick(self.fps)


pg.init()
pg.display.set_caption(c.ORIGINAL_CAPTION)
GAME_SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
board = matrix.Board(GAME_SCREEN)   