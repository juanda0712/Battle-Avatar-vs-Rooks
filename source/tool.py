import pygame as pg
from . import constants as c
from . import game_screen as gs
import os

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
        self.label_title = self.myfont1.render(c.ORIGINAL_TITLE, 1, c.LIGHTYELLOW)
        SCREEN.blit(self.label_title, (c.SCREEN_WIDTH*0.37, c.SCREEN_HEIGHT*0.05))
        #Subtitle
        self.myfont2 = pg.font.SysFont("monospace", c.FONT_SIZE//2)
        self.label_subtitle = self.myfont2.render(c.ORIGINAL_CAPTION, 1, c.LIGHTYELLOW)
        SCREEN.blit(self.label_subtitle, (c.SCREEN_WIDTH*0.315, c.SCREEN_HEIGHT*0.15))

    def text_objects(self,text,font):
        self.text = text
        self.font = font
        self.textSurface = self.font.render(self.text,True,c.BLACK)
        return self.textSurface, self.textSurface.get_rect()

    #Buttons      !PASAR ESTA AFUNCION A COMPONENTES!
    def Initial_buttons(self,msg,x,y,w,h,ic,ac,action=None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        self.smallText = pg.font.Font("freesansbold.ttf",20)

        if x+w > mouse[0] > x and y+h> mouse[1] >y:
            pg.draw.rect(SCREEN,ac,(x,y,w,h))
            if click[0] == 1 and action != None:
                if action == c.NG:
                    self.gameExit = True     
                    game.start_time()
                elif action == c.EX:
                    self.gameExit = True
                    
        
        else:
            pg.draw.rect(SCREEN,ic,(x,y,w,h))
        
        self.textSurf,self.textRect = self.text_objects(msg,self.smallText)
        self.textRect.center = ( (x+(w/2)) , (y+(h/2)) )
        SCREEN.blit(self.textSurf,self.textRect)

    def button_call(self):
        self.Initial_buttons(c.NG,c.X,c.Y,c.X1,c.Y1,c.WHITE,c.GOLD,c.NG)
        self.Initial_buttons(c.LG,c.X,c.Y+50,c.X1,c.Y1,c.WHITE,c.GOLD,c.LG)
        self.Initial_buttons(c.CON,c.X,c.Y+100,c.X1,c.Y1,c.WHITE,c.GOLD,c.CON)
        self.Initial_buttons(c.HOF,c.X,c.Y+150,c.X1,c.Y1,c.WHITE,c.GOLD,c.HOF)
        self.Initial_buttons(c.CR,c.X,c.Y+200,c.X1,c.Y1,c.WHITE,c.GOLD,c.CR)
        self.Initial_buttons(c.HE,c.X,c.Y+250,c.X1,c.Y1,c.WHITE,c.GOLD,c.HE)
        self.Initial_buttons(c.EX,c.X,c.Y+300,c.X1,c.Y1,c.WHITE,c.GOLD,c.EX)


    def main(self):
        while not self.gameExit:  
            self.event_loop()
            SCREEN.fill(c.SKY_BLUE) 
            self.title_game()
            self.button_call()
            pg.display.update()       
            self.clock.tick(self.fps)



pg.init()
game = gs.GameScreen()
pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)