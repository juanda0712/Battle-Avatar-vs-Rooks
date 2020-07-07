
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

    #Buttons
    def Initial_buttons(self):
        mouse = pg.mouse.get_pos()
        self.smallText = pg.font.Font("freesansbold.ttf",20)

        #new game 
        pg.draw.rect(SCREEN,c.WHITE,(c.X,c.Y,c.X1,c.Y1)) 
        self.textSurf,self.textRect = self.text_objects(c.NG,self.smallText)
        self.textRect.center = ( (c.X+(c.X1/2)) , (c.Y+(c.Y1/2)) )
        SCREEN.blit(self.textSurf,self.textRect)
        #load game
        pg.draw.rect(SCREEN,c.WHITE,(c.X,c.Y+50,c.X1,c.Y1))   
        self.textSurf1,self.textRect1 = self.text_objects(c.LG,self.smallText)
        self.textRect1.center = ( (c.X+(c.X1/2)) , (c.Y+(c.Y1/2))+50 )
        SCREEN.blit(self.textSurf1,self.textRect1)
        #Configuration
        pg.draw.rect(SCREEN,c.WHITE,(c.X,c.Y+100,c.X1,c.Y1))   
        self.textSurf2,self.textRect2 = self.text_objects(c.CON,self.smallText)
        self.textRect2.center = ( (c.X+(c.X1/2)) , (c.Y+(c.Y1/2))+100 )
        SCREEN.blit(self.textSurf2,self.textRect2)
        #hall of fame
        pg.draw.rect(SCREEN,c.WHITE,(c.X,c.Y+150,c.X1,c.Y1))   
        self.textSurf3,self.textRect3 = self.text_objects(c.HOF,self.smallText)
        self.textRect3.center = ( (c.X+(c.X1/2)) , (c.Y+(c.Y1/2))+150 )
        SCREEN.blit(self.textSurf3,self.textRect3)
        #credits
        pg.draw.rect(SCREEN,c.WHITE,(c.X,c.Y+200,c.X1,c.Y1))   
        self.textSurf4,self.textRect4 = self.text_objects(c.CR,self.smallText)
        self.textRect4.center = ( (c.X+(c.X1/2)) , (c.Y+(c.Y1/2))+200 )
        SCREEN.blit(self.textSurf4,self.textRect4)
        #help
        pg.draw.rect(SCREEN,c.WHITE,(c.X,c.Y+250,c.X1,c.Y1))   
        self.textSurf5,self.textRect5 = self.text_objects(c.HE,self.smallText)
        self.textRect5.center = ( (c.X+(c.X1/2)) , (c.Y+(c.Y1/2))+250 )
        SCREEN.blit(self.textSurf5,self.textRect5)
        #exit
        pg.draw.rect(SCREEN,c.WHITE,(c.X,c.Y+300,c.X1,c.Y1))   
        self.textSurf6,self.textRect6 = self.text_objects(c.EX,self.smallText)
        self.textRect6.center = ( (c.X+(c.X1/2)) , (c.Y+(c.Y1/2))+300 )
        SCREEN.blit(self.textSurf6,self.textRect6)

    def main(self):
        while not self.gameExit:  
            self.event_loop()
            SCREEN.fill(c.SKY_BLUE)   
            self.title_game()
            self.Initial_buttons()
            pg.display.update()       
            self.clock.tick(self.fps)


pg.init()
pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)