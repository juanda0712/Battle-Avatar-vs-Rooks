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
        self.index  = 0
        self.index2 = 0
        self.index_shoot1 = 0
        self.index_shoot2 = 0
        self.index_shoot3 = 0
        self.index_shoot4 = 0
        self.index_shoot5 = 0
        self.aux=1
        self.aux_av=1
        self.time_avatar = 0


    def create_avatars(self):
        self.time = pg.time.get_ticks()//1000
        if self.aux_av == self.time:
            self.aux_av +=1
            self.time_avatar += 1
        if self.time_avatar ==8:
            self.time_avatar = 0

        if self.time_avatar == 0:

            if random.randint(0,50) <10:
                self.time_avatar = 1
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
        
        

    def create_rooks(self,map_x,map_y,board_game): #detector de torres en la matriz
        maping = board_game.map[map_y][map_x]
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
  
    def draw(self):
        self.time = pg.time.get_ticks()//1000
        self.recorre = 0
        self.create_avatars()

        if self.aux == self.time:
            self.aux +=1
            self.index +=1 
            self.index2 +=1
            self.index_shoot1 += 1
            self.index_shoot2 += 1
            self.index_shoot3 += 1
            self.index_shoot4 += 1
            self.index_shoot5 += 1

        #avatar collision with the row
        for avatar in self.avatars:
            for col in self.rects:
                if avatar.rect.colliderect(col.rect):
                    map_x,map_y = board.getMapIndex(avatar.x,avatar.y)
                    if map_x == 0:
                        self.attack1 = True 
                    else:
                        self.attack1 = False

                    if map_x == 1:
                        self.attack2 = True
                    else:
                        self.attack2 = False

                    if map_x == 2:
                        self.attack3 = True
                    else:
                        self.attack3 = False

                    if map_x == 3:
                        self.attack4 = True
                    else:
                        self.attack4 = False

                    if map_x == 4:
                        self.attack5 = True 
                    else:
                        self.attack5 = False
                        

        if self.index2 == 6:
            self.index2 = 0
        if self.index_shoot1 == 2:
            self.index_shoot1 = 0
        if self.index_shoot2 == 2:
            self.index_shoot2 = 0
        if self.index_shoot3 == 2:
            self.index_shoot3 = 0
        if self.index_shoot4 == 2:
            self.index_shoot4 = 0
        if self.index_shoot5 == 2:
            self.index_shoot5 = 0
        #draw rooks
        for rook in self.rooks:
            rook.draw(self.screen)
            rook.frame = rook.images[self.index2]

            map_x,map_y = board.getMapIndex(rook.x,rook.y)
            if self.attack1 and map_x == 0 and  self.index_shoot1 ==0:
                rook.shoot()
                self.index_shoot1 =1
                
            elif self.attack2 and map_x ==1 and self.index_shoot2 ==0:
                rook.shoot() 
                self.index_shoot2 =1

            elif self.attack3 and map_x ==2 and self.index_shoot3 ==0:
                rook.shoot() 
                self.index_shoot3 =1
                  
            elif self.attack4 and map_x ==3 and  self.index_shoot4 ==0:
                rook.shoot()   
                self.index_shoot4 =1

            elif self.attack5 and map_x==4 and  self.index_shoot5 ==0:
                rook.shoot()
                self.index_shoot5 = 1

            if rook.shootList != []:
                rook.draw_shoot(self.screen)

            for bullet in rook.shootList:

                if bullet.rect.centery >= c.F_BULLET:
                    rook.shootList.remove(bullet)
                
                
            

            
        
        #draw avatars
        if self.index == 4:
            self.index = 0    
        for avatar in self.avatars:
            avatar.draw(self.screen)
            avatar.rect.centery -=0.18
            avatar.frame = avatar.images[self.index]

            
        #draw rectangles in the rows
        for rect in self.rects:
            rect.draw_rect(self.screen)

        
board = matrix.Board()
