from . import constants as c
from . import prueba_mouse as pm
import pygame as pg
from .component import matrix, timer, name
from threading import Thread
import time



class GameScreen:
    
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.gameExit = False
        self.clock = pg.time.Clock()
        self.fps = 60
        self.begin = time.time()
        self.minutes = 0
        self.hours = 0

        

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                show_time.break_loop()
                name.break_loop()
                self.gameExit = True
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                print(f'Posicion: {board.showRooks(x,y)}')
                board.showGrid(x,y)
                for i in board.showMap():
                    print(i)
    
    def call_time(self):
        list1 = show_time.count(self.begin)
        if int(list1[0]) == 60:
            self.begin = time.time()
            list1[0] = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes =0
            self.hours +=1
        
        output = show_time.smallText.render("Tiempo: "+ str(self.hours)+":"+str(self.minutes)+":"+str(int(list1[0])),0,c.BLACK)
        self.screen.blit(output,c.TIME_POS)



    def main(self):
        #self.start_animation()
        while not self.gameExit:  
            self.event_loop()
            GAME_SCREEN.fill(c.LIGHTYELLOW)  
            board.create_board()
            board.detect()
            #pm.pos()
            self.call_time()
            name.show_name()
            pg.display.update()       

            self.clock.tick(self.fps)


pg.init()
pg.display.set_caption(c.ORIGINAL_CAPTION)
GAME_SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
board = matrix.Board(GAME_SCREEN)
show_time  = timer.Timer(GAME_SCREEN,True)
name = name.Name(GAME_SCREEN,True)
