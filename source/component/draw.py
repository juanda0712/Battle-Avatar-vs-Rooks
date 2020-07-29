from . import avatars,coins,matrix,rooks
from .blocks import *
from .. import constants as c
import pygame as pg
import random
import time


class Painter:
    def __init__(self,screen):
        self.screen = screen
        self.avatars = []
        self.rooks = []
        self.rook_type = 0
        self.rects = [Block(c.OFFSET_X,c.OFFSET_Y,65,585),
            Block(c.OFFSET_X+65,c.OFFSET_Y,65,585),
            Block(c.OFFSET_X+130,c.OFFSET_Y,65,585),
            Block(c.OFFSET_X+195,c.OFFSET_Y,65,585),
            Block(c.OFFSET_X+260,c.OFFSET_Y,65,585)]
        self.attack1 = False
        self.attack2 = False
        self.attack3 = False
        self.attack4 = False
        self.attack5 = False
        
    


    def create_avatars(self):

        if random.randint(0,230) == 1:
            col = random.randint(0,4)
            x,y = board.getMapGridPos(col,8)
            ava = random.randint(1,4)
            if ava == 1:
                self.avatars.append(avatars.Avatar_archer(x,y+60,1,1))
            elif ava == 2:
                self.avatars.append(avatars.Avatar_tank(x,y+60,1,1))
            elif ava == 3:
                self.avatars.append(avatars.Avatar_lumberjack(x,y+60,1,1))
            else:
                self.avatars.append(avatars.Avatar_cannibal(x,y+60,1,1))
    
        
    def set_rook_type(self,type):
        self.type = type
        if self.type == "Sand Rook":
            self.rook_type = 1
        elif self.type == "Rock Rook":
            self.rook_type = 2
        elif self.type == "Fire Rook":
            self.rook_type = 3
        elif self.type == "Water Rook":
            self.rook_type = 4
        
        

    def create_rooks(self,map_x,map_y,board_game):
        maping = board_game.map[map_y][map_x]
        print(maping)
        x,y = board.getMapGridPos(map_x,map_y)
        if maping == 1:
            self.rooks.append(rooks.Sand_rook(x,y,5))
        elif maping == 2:
            self.rooks.append(rooks.Rock_rook(x,y,5))
        elif maping == 3:
            self.rooks.append(rooks.Fire_rook(x,y,5))
        elif maping == 4:
            self.rooks.append(rooks.Water_rook(x,y,5))        
        

    def update(self):
        pass
    
    """def detect_collide(self):
        for rect in self.rects:"""




    def draw(self):
        self.recorre = 0
        
        for avatar in self.avatars:
            for i in self.rects:
                if avatar.rect.colliderect(i.rect):
                    map_x,map_y = board.getMapIndex(avatar.x,avatar.y)
                    if map_x == 0:
                        self.attack1 = True            
                    elif map_x == 1:
                        self.attack2 = True
                    elif map_x == 2:
                        self.attack3 = True
                    elif map_x == 3:
                        self.attack4 = True
                    elif map_x == 4:
                        self.attack5 = True                   


        for i in self.rooks:
            i.draw(self.screen)
            i.shoot()
            for m in i.shootList:
                map_x,map_y = board.getMapIndex(i.x,i.y)
                if self.attack1 and map_x == 0:
                        i.draw_shoot(self.screen)
                elif self.attack2 and map_x ==1 :
                        i.draw_shoot(self.screen)
                elif self.attack3 and map_x ==2:
                        i.draw_shoot(self.screen)
                elif self.attack4 and map_x ==3:
                        i.draw_shoot(self.screen)
                elif self.attack5 and map_x == 4:
                        i.draw_shoot(self.screen)
                
                
        
    
        for i in self.avatars:
            i.draw(self.screen)
            i.rect.centery -=0.18
        
        for i in self.rects:
            i.draw_rect(self.screen)

        
board = matrix.Board()
