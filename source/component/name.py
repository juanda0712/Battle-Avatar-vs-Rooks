import pygame as pg
from .. import constants as c 

class Name:
    def __init__(self,screen,state):
        self.screen = screen
        self.smallText = pg.font.SysFont("monospace", c.FONT_SIZE_TIMER)
        self.loop = state

    def break_loop(self):
        self.loop = False

    def show_name(self):
        output = self.smallText.render("Player name: Player 1",0,c.BLACK)
        self.screen.blit(output,c.NAME_POS)
        