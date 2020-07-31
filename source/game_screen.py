from . import constants as c
from . import prueba_mouse as pm
import pygame as pg
from .component import matrix, timer, name , avatars, draw
from threading import Thread
import time
import os



class GameScreen:
    
    def __init__(self):
        self.bg = pg.image.load(os.path.join(c.PATH,"background","Fondo01.png"))
        self.screen = pg.display.get_surface()
        self.gameExit = False
        self.clock = pg.time.Clock()
        self.fps = 30
        self.begin = time.time()
        self.minutes = 0
        self.hours = 0
#--------------EVENTOS--------------------------------------------------#
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                show_time.break_loop()
                name.break_loop()
                self.gameExit = True
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                map_x,map_y = board.getMapIndex(x,y)
                pos_x,pos_y = board.getMapGridPos(map_x,map_y)
                if board.isValid(map_x,map_y) and board.isMovable(map_x, map_y):
                    board.setMapGridType(map_x,map_y,draw.rook_type)
                    draw.create_rooks(map_x,map_y,board,draw.rook_type)
                    draw.rook_type = 0
                    
                if draw.coins_exist == 1:
                    if pos_x == draw.star[0].x and pos_y == draw.star[0].y and draw.rook_type ==0:
                        draw.star.pop(0)
                        draw.money +=50
                        draw.coins_exist = 0

                    

                print(f'Posicion: {board.showRooks(x,y)}')
                #board.getGridType(x,y)
                for i in board.showMap():
                    print(i)
                    
#---------------TIMER---------------------------------------------------
    def start_time(self):
        self.begin = time.time()
        self.main()

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


#----------------------BUTTONS------------------------------------------#
    def text_objects(self,text,font):
        self.text = text
        self.font = font
        self.textSurface = self.font.render(self.text,True,c.BLACK)
        return self.textSurface, self.textSurface.get_rect()

    def game_buttons(self,msg,x,y,w,h,ic,ac,action=None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        self.smallText = pg.font.Font("freesansbold.ttf",20)

        if x+w > mouse[0] > x and y+h> mouse[1] >y:
            pg.draw.rect(GAME_SCREEN,ac,(x,y,w,h))
            if click[0] == 1 and action != None:
                if action == 1:
                    draw.set_rook_type(c.SR)
                elif action == 2:
                    draw.set_rook_type(c.RR)
                elif action == 3:
                    draw.set_rook_type(c.FR) 
                elif action == 4:
                    draw.set_rook_type(c.WR)        
        else:
            pg.draw.rect(GAME_SCREEN,ic,(x,y,w,h))
        
        self.textSurf,self.textRect = self.text_objects(msg,self.smallText)
        self.textRect.center = ( (x+(w/2)) , (y+(h/2)) )
        GAME_SCREEN.blit(self.textSurf,self.textRect)

    def button_call(self):
        self.game_buttons(c.SR1,c.X_GAME,c.Y_GAME+50,c.X1,c.Y1,c.WHITE,c.GOLD,1)
        self.game_buttons(c.RR1,c.X_GAME,c.Y_GAME+100,c.X1,c.Y1,c.WHITE,c.LIGHTBROWN,2)
        self.game_buttons(c.FR1,c.X_GAME,c.Y_GAME+150,c.X1,c.Y1,c.WHITE,c.RED,3)
        self.game_buttons(c.WR1,c.X_GAME,c.Y_GAME+200,c.X1,c.Y1,c.WHITE,c.SKY_BLUE,4)
 

#----------------------MAIN--------------------------------------------#

    def main(self):
        
        while not self.gameExit:
             
            self.event_loop() #captura eventos
            pg.display.update()
            GAME_SCREEN.fill(c.FONT_GREEN)   #color del fondo 
            self.screen.blit(self.bg,(c.OFFSET_X-57,c.OFFSET_Y-55)) 
            self.button_call()    #Los botones de las torres
            draw.draw()             #dibuja los 
            self.call_time()    #timpo
            name.show_name()    #Nombre jugador
            self.clock.tick(self.fps)
               

            


pg.init()
pg.display.set_caption(c.ORIGINAL_CAPTION)
GAME_SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
board = matrix.Board()
show_time  = timer.Timer(GAME_SCREEN,True)
name = name.Name(GAME_SCREEN,True)
draw = draw.Painter(GAME_SCREEN,board)
