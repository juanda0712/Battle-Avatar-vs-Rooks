from . import avatars,matrix,rooks ,coins  
from .blocks import *
from .. import constants as c
import pygame as pg
import random
import time
import os


class Painter:
    def __init__(self,screen,board): 
        self.board = board
        self.screen = screen
        self.avatars = []
        self.rooks = []
        self.star = []
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
        self.index_shoot2 = 1
        self.index_shoot3 = 2
        self.index_shoot4 = 3
        self.index_shoot5 = 0
        self.shoot_time_avatar1 = 0
        self.shoot_time_avatar2 = 0
        self.shoot_time_avatar3 = 0
        self.shoot_time_avatar4 = 0
        self.shoot_time_avatar5 = 0
        self.aux=1
        self.aux_av=1
        self.aux_coins=1
        self.coins_exist = 0
        self.time_avatar = 0
        self.money = 1000
        self.smallText = pg.font.SysFont("monospace", c.FONT_SIZE_TIMER)
        
        


    def create_avatars(self):
        self.time = pg.time.get_ticks()//1000
        if self.aux_av == self.time:
            self.aux_av +=1
            self.time_avatar += 1
        if self.time_avatar == 5:
            self.time_avatar = 0

        if self.time_avatar == 0:
            self.time_avatar = 1
            if random.randint(0,10) <= 7:
                col = random.randint(0,4)
                x,y = self.board.getMapGridPos(col,8)
                ava = random.randint(1,4)
                if ava == 1:
                    self.avatars.append(avatars.Avatar_archer(x,y+25,1,1))
                elif ava == 2:
                    self.avatars.append(avatars.Avatar_tank(x,y+25,1,1))
                elif ava == 3:
                    self.avatars.append(avatars.Avatar_lumberjack(x,y+25,1,1))
                else:
                    self.avatars.append(avatars.Avatar_cannibal(x,y+25,1,1))
    
        
    def set_rook_type(self,type):
        self.type = type
        if self.type == "Sand Rook" and self.money >=50:
            self.rook_type = 1
            
        elif self.type == "Rock Rook"and self.money >=100:
            self.rook_type = 2
            
        elif self.type == "Fire Rook"and self.money >=150:
            self.rook_type = 3
            
        elif self.type == "Water Rook"and self.money >=150:
            self.rook_type = 4
            
        
        

    def create_rooks(self,map_x,map_y,board_game,type): #detector de torres en la matriz
        self.type = type 
        maping = board_game.map[map_y][map_x]
        x,y = self.board.getMapGridPos(map_x,map_y)
        
        if maping == 1:
            self.rooks.append(rooks.Sand_rook(x,y,5))
        elif maping == 2:
            self.rooks.append(rooks.Rock_rook(x,y,5))
        elif maping == 3:
            self.rooks.append(rooks.Fire_rook(x,y,5))
        elif maping == 4:
            self.rooks.append(rooks.Water_rook(x,y,5))  

        if self.type == 1 and self.money >=50:
            self.money -= 50
        elif self.type == 2 and self.money >= 100:
            self.money -=100
        elif self.type > 2 and self.type <= 4:
            self.money -= 150



#----------------------------COINS------------------------------------------#
    def coins(self,value):
        self.value = value
        output1 = self.smallText.render('Coins: '+str(self.value),0,c.BLACK)
        self.screen.blit(output1, (10,10))

    def draw_alec_coins(self):
        while self.star != [] and self.aux_coins == 0:
            self.star.pop(0)
            self.coins_exist = 0
        if self.aux_coins == 0:
            map_x,map_y = self.board.getRandomMapIndex()
            pos_x,pos_y = self.board.getMapGridPos(map_x, map_y)
            self.star.append(coins.Coins(pos_x,pos_y))
            self.aux_coins =1
            self.coins_exist = 1

#--------------------------DRAW--------------------------------------------#
    def draw(self):
        self.time = pg.time.get_ticks()//1000
        self.recorre = 0
        self.create_avatars()
        self.coins(self.money)
        self.draw_alec_coins()

        if self.aux == self.time:
            self.aux +=1
            self.index +=1 
            self.index2 +=1
            self.index_shoot1 += 1
            self.index_shoot2 += 1
            self.index_shoot3 += 1
            self.index_shoot4 += 1
            self.index_shoot5 += 1
            self.aux_coins +=1
            self.shoot_time_avatar1 += 1
            self.shoot_time_avatar2 += 1
            self.shoot_time_avatar3 += 1
            self.shoot_time_avatar4 += 1
            self.shoot_time_avatar5 += 1

        #avatar collisions
        for avatar in self.avatars:     
            #with row
            for col in self.rects:
                if avatar.rect.colliderect(col.rect):
                    map_x,map_y = self.board.getMapIndex(avatar.x,avatar.y)
                    if map_x == 0:
                        self.attack1 = True 
                    if map_x == 1:
                        self.attack2 = True
                    if map_x == 2:
                        self.attack3 = True
                    if map_x == 3:
                        self.attack4 = True
                    if map_x == 4:
                        self.attack5 = True 
            #with rooks
            for rook in self.rooks:
                if avatar.rect.colliderect(rook.rect):
                    avatar.avatar_move = False
                """else:
                    self.avatar_move = True"""

            #with other avatar
            for avatar2 in self.avatars:
                if avatar.rect.colliderect(avatar2.rect) and avatar.range ==2 and avatar2.range ==2 and avatar != avatar2:
                    avatar2.avatar_move = False

            for avatar3 in self.avatars:
                if avatar.rect.colliderect(avatar3.rect) and avatar.range ==1 and avatar3.range ==1 and avatar != avatar3:
                    self.avatars.remove(avatar3)


            #rook collide with rect
            for rook in self.rooks:
                for col in self.rects:
                    if rook.rect.colliderect(col.rect):
                        map_x,map_y = self.board.getMapIndex(rook.x,rook.y)
                        for avatar2 in self.avatars:
                            map_xa,map_ya = self.board.getMapIndex(avatar2.x,avatar2.y)
                            if avatar2.range == 1:
                                if map_x == map_xa:
                                    avatar2.avatar_move = False

            

 
        if self.index2 == 6:
            self.index2 = 0
        if self.index_shoot1 == 4:
            self.index_shoot1 = 0
        if self.index_shoot2 == 4:
            self.index_shoot2 = 0
        if self.index_shoot3 == 4:
            self.index_shoot3 = 0
        if self.index_shoot4 == 4:
            self.index_shoot4 = 0
        if self.index_shoot5 == 4:
            self.index_shoot5 = 0
        if self.aux_coins == 10:
            self.aux_coins = 0
        if self.shoot_time_avatar1 == 3:
            self.shoot_time_avatar1 = 0
        if self.shoot_time_avatar2 == 3:
            self.shoot_time_avatar2 = 0
        if self.shoot_time_avatar3 == 3:
            self.shoot_time_avatar3 = 0
        if self.shoot_time_avatar4 == 3:
            self.shoot_time_avatar4 = 0
        if self.shoot_time_avatar5 == 3:
            self.shoot_time_avatar5 = 0



        #draw stars
        for coin in self.star:
            coin.draw(self.screen)

        #draw rooks
        for rook in self.rooks:
            rook.draw(self.screen)
            rook.frame = rook.images[self.index2]

            map_x,map_y = self.board.getMapIndex(rook.x,rook.y)
            if self.attack1 and map_x == 0 :
                if rook.shootList != []:
                    rook.draw_shoot(self.screen)
                if self.index_shoot1 ==0:
                    for rook in self.rooks:
                        map_x,map_y = self.board.getMapIndex(rook.x,rook.y)
                        if map_x == 0:
                            rook.shoot()
                                               
                    self.index_shoot1 =1
                
            elif self.attack2 and map_x == 1 :
                if rook.shootList != []:
                    rook.draw_shoot(self.screen)
                if self.index_shoot2 ==0:
                
                    for rook in self.rooks:
                        map_x,map_y = self.board.getMapIndex(rook.x,rook.y)
                        if map_x == 1:
                            rook.shoot()
                          
                    self.index_shoot2 =1

            elif self.attack3 and map_x == 2 :
                if rook.shootList != []:
                    rook.draw_shoot(self.screen)
                if self.index_shoot3 ==0:
                
                    for rook in self.rooks:
                        map_x,map_y = self.board.getMapIndex(rook.x,rook.y)
                        if map_x == 2:
                            rook.shoot()
                                             
                    self.index_shoot3 =1
                  
            elif self.attack4 and map_x == 3 :
                if rook.shootList != []:
                    rook.draw_shoot(self.screen)
                if self.index_shoot4 ==0:
                
                    for rook in self.rooks:
                        map_x,map_y = self.board.getMapIndex(rook.x,rook.y)
                        if map_x == 3:
                            rook.shoot()
                                        
                    self.index_shoot4 = 1

            if self.attack5 and map_x == 4 :
                if rook.shootList != []:
                    rook.draw_shoot(self.screen)
                if self.index_shoot5 ==0:
                
                    for rook in self.rooks:
                        map_x,map_y = self.board.getMapIndex(rook.x,rook.y)
                        if map_x == 4:
                            rook.shoot() 
                            
                    self.index_shoot5 =1

        
            #Elimina bullet and avatars
            for bullet in rook.shootList:

                if bullet.rect.centery >= c.F_BULLET:
                    rook.shootList.remove(bullet)

                for avatar in self.avatars:
                    if bullet.rect.colliderect(avatar.rect):
                        rook.shootList.remove(bullet)
                        avatar.health -= 1
                    
                    if avatar.health  <=0:
                        self.avatars.remove(avatar)
                        self.money += 100
                        map_x,map_y = self.board.getMapIndex(avatar.x,avatar.y)
                        if map_x == 0:
                            self.attack1 = False 
                            for rook in self.rooks:
                                x,y = self.board.getMapIndex(rook.x,rook.y)
                                if x ==0:
                                    while rook.shootList != [] and map_x == 0:
                                            rook.shootList.pop(0)
                        if map_x == 1:
                            self.attack2 = False
                            for rook in self.rooks:
                                x,y = self.board.getMapIndex(rook.x,rook.y)
                                if x ==1:
                                    while rook.shootList != []and map_x == 1:
                                            rook.shootList.pop(0)
                        if map_x == 2:
                            self.attack3 = False
                            for rook in self.rooks:
                                x,y = self.board.getMapIndex(rook.x,rook.y)
                                if x ==2:
                                    while rook.shootList != [] and map_x == 2:
                                            rook.shootList.pop(0)
                        if map_x == 3:
                            self.attack4 = False
                            for rook in self.rooks:
                                x,y = self.board.getMapIndex(rook.x,rook.y)
                                if x ==3:
                                    while rook.shootList != [] and map_x == 3:
                                            rook.shootList.pop(0)
                        if map_x == 4:
                            self.attack5 = False 
                            for rook in self.rooks:
                                x,y = self.board.getMapIndex(rook.x,rook.y)
                                if x ==4:
                                    while rook.shootList != [] and map_x == 4:
                                            rook.shootList.pop(0)

            #Bullet Collision with the rooks
            for avatar in self.avatars:
                if avatar.range ==1:
                    for shoot in avatar.shootList :
                        if rook.rect.colliderect(shoot.rect) :
                            avatar.shootList.remove(shoot)
                            rook.health -= 5
                        if rook.health <= 0:
                            self.board.map[map_y][map_x] = 0
                            self.rooks.remove(rook)
                            avatar.avatar_move = True

            


            


                
        #draw avatars
        if self.index == 4:
            self.index = 0    
        for avatar in self.avatars:
            map_x,map_y = self.board.getMapIndex(avatar.x,avatar.y)
            if avatar.avatar_move:
                avatar.draw(self.screen)
                avatar.rect.centery -=0.18
                avatar.frame = avatar.images[self.index]
            elif not avatar.avatar_move:
                avatar.draw(self.screen)
                avatar.frame = avatar.images[self.index]

            
            if  avatar.avatar_move == False and avatar.range ==1 and map_x == 0:
                if avatar.shootList != []:
                    avatar.draw_shoot(self.screen)

                if  self.shoot_time_avatar1 == 0:
                    for avatar2 in self.avatars:
                        map_x,map_y = self.board.getMapIndex(avatar2.x,avatar2.y)
                        if map_x == 0 and avatar2.range==1:
                            avatar2.shoot() 
                    
                    self.shoot_time_avatar1 = 1

            elif  avatar.avatar_move == False and avatar.range ==1 and map_x == 1:
                if avatar.shootList != []:
                    avatar.draw_shoot(self.screen)

                if  self.shoot_time_avatar2 == 0:
                    for avatar2 in self.avatars:
                        map_x,map_y = self.board.getMapIndex(avatar2.x,avatar2.y)
                        if map_x == 1 and avatar2.range==1:
                            avatar2.shoot() 
                    
                    self.shoot_time_avatar2 = 1

            elif  avatar.avatar_move == False and avatar.range ==1 and map_x == 2:
                if avatar.shootList != []:
                    avatar.draw_shoot(self.screen)

                if  self.shoot_time_avatar3 == 0:
                    for avatar2 in self.avatars:
                        map_x,map_y = self.board.getMapIndex(avatar2.x,avatar2.y)
                        if map_x == 2 and avatar2.range==1:
                            avatar2.shoot() 
                    
                    self.shoot_time_avatar3 = 1

            elif  avatar.avatar_move == False and avatar.range ==1 and map_x == 3:
                if avatar.shootList != []:
                    avatar.draw_shoot(self.screen)

                if  self.shoot_time_avatar4 == 0:
                    for avatar2 in self.avatars:
                        map_x,map_y = self.board.getMapIndex(avatar2.x,avatar2.y)
                        if map_x == 3 and avatar2.range==1:
                            avatar2.shoot() 
                    
                    self.shoot_time_avatar4 = 1

            elif  avatar.avatar_move == False and avatar.range ==1 and map_x == 4:
                if avatar.shootList != []:
                    avatar.draw_shoot(self.screen)

                if  self.shoot_time_avatar5 == 0:
                    for avatar2 in self.avatars:
                        map_x,map_y = self.board.getMapIndex(avatar2.x,avatar2.y)
                        if map_x == 4 and avatar2.range==1:
                            avatar2.shoot() 
                    
                    self.shoot_time_avatar5 = 1
                    
        #draw rectangles in the rows
        for rect in self.rects:
            rect.draw_rect(self.screen)

        
#board = matrix.Board()

