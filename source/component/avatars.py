import pygame as pg
from .. import constants as c 
import os


class Avatar_archer():  #1
    def __init__(self,x,y,mov_speed, attack_speed ):
        self.x = x
        self.y = y
        self.health = 5
        self.damage = 2
        self.mov_speed = mov_speed
        self.attack_speed = attack_speed
        """self.imagenA = pg.image.load(os.path.join(c.PATH,"avatars/archer","Archer01.png"))
        self.imagenB = pg.image.load(os.path.join(c.PATH,"avatars/archer","Archer02.png"))
        self.imagenC = pg.image.load(os.path.join(c.PATH,"avatars/archer","Archer03.png"))
        self.imagenD = pg.image.load(os.path.join(c.PATH,"avatars/archer","Archer04.png"))"""

        self.imagenA = pg.image.load('images\\avatars\\archer\\Archer01.png')
        self.imagenB = pg.image.load('images\\avatars\\archer\\Archer02.png')
        self.imagenC = pg.image.load('images\\avatars\\archer\\Archer03.png')
        self.imagenD = pg.image.load('images\\avatars\\archer\\Archer04.png')
        #C:\\Users\\The Folder\\WorldMap.jpg
        self.images = [self.imagenA,self.imagenB,self.imagenC,self.imagenD]
        self.indexImages = 0
        self.frame = self.images[self.indexImages]
        self.rect = self.frame.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self,screen):
        screen.blit(self.frame,self.rect)


class Avatar_tank():  #2
    def __init__(self,x,y,mov_speed, attack_speed ):
        self.x = x
        self.y = y
        self.health = 10
        self.damage = 3
        self.mov_speed = mov_speed
        self.attack_speed = attack_speed
        self.imagenA = pg.image.load(os.path.join(c.PATH,"avatars/tank","Tank01.png"))
        self.imagenB = pg.image.load(os.path.join(c.PATH,"avatars/tank","Tank02.png"))
        self.imagenC = pg.image.load(os.path.join(c.PATH,"avatars/tank","Tank03.png"))
        self.imagenD = pg.image.load(os.path.join(c.PATH,"avatars/tank","Tank04.png"))
        self.images = [self.imagenA,self.imagenB,self.imagenC,self.imagenD]
        self.indexImages = 0
        self.frame = self.images[self.indexImages]
        self.rect = self.frame.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self,screen):
        screen.blit(self.frame,self.rect)

  
class Avatar_lumberjack():  #3
    def __init__(self,x,y,mov_speed, attack_speed ):
        self.x = x
        self.y = y
        self.health = 20
        self.damage = 9
        self.mov_speed = mov_speed
        self.attack_speed = attack_speed
        
        self.imagenA = pg.image.load(os.path.join(c.PATH,"avatars/Lumberjack","Lumberjack01.png"))
        self.imagenB = pg.image.load(os.path.join(c.PATH,"avatars/Lumberjack","Lumberjack02.png"))
        self.imagenC = pg.image.load(os.path.join(c.PATH,"avatars/Lumberjack","Lumberjack03.png"))
        self.imagenD = pg.image.load(os.path.join(c.PATH,"avatars/Lumberjack","Lumberjack04.png")) 
        self.images = [self.imagenA,self.imagenB,self.imagenC,self.imagenD]
        self.indexImages = 0
        self.frame = self.images[self.indexImages]
        self.rect = self.frame.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self,screen):
        screen.blit(self.frame,self.rect)


class Avatar_cannibal(): #4
    def __init__(self,x,y,mov_speed, attack_speed ):
        self.x = x
        self.y = y
        self.health = 25
        self.damage = 12
        self.mov_speed = mov_speed
        self.attack_speed = attack_speed
        self.imagenA = pg.image.load(os.path.join(c.PATH,"avatars/Cannibal","Cannibal01.png"))
        self.imagenB = pg.image.load(os.path.join(c.PATH,"avatars/Cannibal","Cannibal02.png"))
        self.imagenC = pg.image.load(os.path.join(c.PATH,"avatars/Cannibal","Cannibal03.png"))
        self.imagenD = pg.image.load(os.path.join(c.PATH,"avatars/Cannibal","Cannibal04.png"))  
        self.images = [self.imagenA,self.imagenB,self.imagenC,self.imagenD]
        self.indexImages = 0
        self.frame = self.images[self.indexImages]
        self.rect = self.frame.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self,screen):
        screen.blit(self.frame,self.rect)











    

    
        