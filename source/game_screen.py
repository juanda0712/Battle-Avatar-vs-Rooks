from . import constants as c
import pygame as pg
from .component import matrix, timer
from threading import Thread
import threading 


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
    
    def start_animation(self):
        """board_thread = Thread(target=board.create_board)
        board_thread.daemon = True
        board_thread.start()"""

        time_thread = Thread(target=time.count)
        time_thread.daemon = True
        time_thread.start()

    def main(self):
        self.start_animation()
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
time  = timer.Timer()