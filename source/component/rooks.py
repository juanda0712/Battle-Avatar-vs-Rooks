import pygame as pg
from .. import constants as c 
import os

class Sand_rook: #!
    def __init__(self,x,y,attack_speed):
        self.x = x
        self.y = y
        self.health = 7
        self.damage = 2
        self.price = 100
        self.attack_speed = attack_speed
        self.imagenA = pg.image.load(os.path.join(c.PATH,"Rooks/SandRook","SandRook01.png"))
        self.imagenB = pg.image.load(os.path.join(c.PATH,"Rooks/SandRook","SandRook02.png"))
        self.imagenC = pg.image.load(os.path.join(c.PATH,"Rooks/SandRook","SandRook03.png"))
        self.imagenD = pg.image.load(os.path.join(c.PATH,"Rooks/SandRook","SandRook04.png"))
        self.imagenE = pg.image.load(os.path.join(c.PATH,"Rooks/SandRook","SandRook05.png"))
        self.imagenF = pg.image.load(os.path.join(c.PATH,"Rooks/SandRook","SandRook06.png"))
        self.images = [self.imagenA,self.imagenB,self.imagenC,self.imagenD,self.imagenE,self.imagenF]
        self.indexImages = 0
        self.frame = self.images[self.indexImages]
        self.rect = self.frame.get_rect()
        self.rect.centerx = x
        self.rect.centery = y-6
        self.shootList = []
        self.index = 0

    def draw(self,screen):
        screen.blit(self.frame,self.rect)


    def shoot(self):
        self.shootList.append(Bullet(self.x,self.y,self.damage))

    def draw_shoot(self,screen):
        for bullet in self.shootList: 
            bullet.direction()
            bullet.draw_bullet(screen)


class Rock_rook: #2
    def __init__(self,x,y,attack_speed):
        self.x = x
        self.y = y
        self.health = 14
        self.damage = 4
        self.price = 150
        self.attack_speed = attack_speed
        self.imagenA = pg.image.load(os.path.join(c.PATH,"Rooks/RockRook","RockRook01.png"))
        self.imagenB = pg.image.load(os.path.join(c.PATH,"Rooks/RockRook","RockRook02.png"))
        self.imagenC = pg.image.load(os.path.join(c.PATH,"Rooks/RockRook","RockRook03.png"))
        self.imagenD = pg.image.load(os.path.join(c.PATH,"Rooks/RockRook","RockRook04.png"))
        self.imagenE = pg.image.load(os.path.join(c.PATH,"Rooks/RockRook","RockRook05.png"))
        self.imagenF = pg.image.load(os.path.join(c.PATH,"Rooks/RockRook","RockRook06.png"))
        self.images = [self.imagenA,self.imagenB,self.imagenC,self.imagenD,self.imagenE,self.imagenF]
        self.indexImages = 0
        self.frame = self.images[self.indexImages]
        self.rect = self.frame.get_rect()
        self.rect.centerx = x
        self.rect.centery = y-6
        self.shootList = []

    def draw(self,screen):
        screen.blit(self.frame,self.rect)

    def shoot(self):
        self.shootList.append(Bullet(self.x,self.y,self.damage))
    
    def draw_shoot(self,screen):
        for bullet in self.shootList: 
            bullet.direction()
            bullet.draw_bullet(screen)
class Fire_rook: #3
    def __init__(self,x,y,attack_speed):
        self.x = x
        self.y = y
        self.health = 16
        self.damage = 8
        self.price = 150
        self.attack_speed = attack_speed
        self.imagenA = pg.image.load(os.path.join(c.PATH,"Rooks/FireRook","FireRook01.png"))
        self.imagenB = pg.image.load(os.path.join(c.PATH,"Rooks/FireRook","FireRook02.png"))
        self.imagenC = pg.image.load(os.path.join(c.PATH,"Rooks/FireRook","FireRook03.png"))
        self.imagenD = pg.image.load(os.path.join(c.PATH,"Rooks/FireRook","FireRook04.png"))
        self.imagenE = pg.image.load(os.path.join(c.PATH,"Rooks/FireRook","FireRook05.png"))
        self.imagenF = pg.image.load(os.path.join(c.PATH,"Rooks/FireRook","FireRook06.png"))
        self.images = [self.imagenA,self.imagenB,self.imagenC,self.imagenD,self.imagenE,self.imagenF]
        self.indexImages = 0
        self.frame = self.images[self.indexImages]
        self.rect = self.frame.get_rect()
        self.rect.centerx = x
        self.rect.centery = y-6
        self.shootList = []

    def draw(self,screen):
        screen.blit(self.frame,self.rect)

    def shoot(self):
        self.shootList.append(Bullet(self.x,self.y,self.damage))

    def draw_shoot(self,screen):
        for bullet in self.shootList: 
            bullet.direction()
            bullet.draw_bullet(screen)

class Water_rook: #4
    def __init__(self,x,y,attack_speed):
        self.x = x
        self.y = y
        self.health = 16
        self.damage = 8
        self.price = 150
        self.attack_speed = attack_speed
        self.imagenA = pg.image.load(os.path.join(c.PATH,"Rooks/WaterRook","WaterRook01.png"))
        self.imagenB = pg.image.load(os.path.join(c.PATH,"Rooks/WaterRook","WaterRook02.png"))
        self.imagenC = pg.image.load(os.path.join(c.PATH,"Rooks/WaterRook","WaterRook03.png"))
        self.imagenD = pg.image.load(os.path.join(c.PATH,"Rooks/WaterRook","WaterRook04.png"))
        self.imagenE = pg.image.load(os.path.join(c.PATH,"Rooks/WaterRook","WaterRook05.png"))
        self.imagenF = pg.image.load(os.path.join(c.PATH,"Rooks/WaterRook","WaterRook06.png"))
        self.images = [self.imagenA,self.imagenB,self.imagenC,self.imagenD,self.imagenE,self.imagenF]
        self.indexImages = 0
        self.frame = self.images[self.indexImages]
        self.rect = self.frame.get_rect()
        self.rect.centerx = x
        self.rect.centery = y-6
        self.shootList = []

    def draw(self,screen):
        screen.blit(self.frame,self.rect)

    def shoot(self):
        self.shootList.append(Bullet(self.x,self.y,self.damage))

    def draw_shoot(self,screen):
        for bullet in self.shootList: 
            bullet.direction()
            bullet.draw_bullet(screen)

            
        

class Bullet:
    def __init__(self,x,y,damage):
        self.damage = damage
        self.imagenA = pg.image.load(os.path.join(c.PATH,"bullets","SandRook.png"))
        self.rect = self.imagenA.get_rect()
        self.rect.centerx = x
        self.rect.centery = y-6
        self.speed = 5

    def direction(self):
        self.rect.centery += self.speed
        

    def draw_bullet(self,screen):
        screen.blit(self.imagenA,self.rect)
