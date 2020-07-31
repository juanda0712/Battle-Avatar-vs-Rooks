import pygame as pg
from .. import constants as c 
import os


class Avatar_archer():  #1
    def __init__(self,x,y,mov_speed, attack_speed ):
        self.range = 1 
        self.x = x
        self.y = y
        self.avatar_move = True
        self.health = 5
        self.damage = 2
        self.mov_speed = mov_speed
        self.attack_speed = attack_speed
        self.imagenA = pg.image.load(os.path.join(c.PATH,"avatars/archer","Archer01.png"))
        self.imagenB = pg.image.load(os.path.join(c.PATH,"avatars/archer","Archer02.png"))
        self.imagenC = pg.image.load(os.path.join(c.PATH,"avatars/archer","Archer03.png"))
        self.imagenD = pg.image.load(os.path.join(c.PATH,"avatars/archer","Archer04.png"))
        self.images = [self.imagenA,self.imagenB,self.imagenC,self.imagenD]
        self.indexImages = 0
        self.frame = self.images[self.indexImages]
        self.rect = self.frame.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.shootList = []

    def draw(self,screen):
        screen.blit(self.frame,self.rect)

    def shoot(self):
        self.shootList.append(Bullet(self.rect.centerx,self.rect.centery,self.damage,1))

    def draw_shoot(self,screen):
        for bullet in self.shootList: 
            bullet.direction()
            bullet.draw_bullet(screen,1)

        


class Avatar_tank():  #2
    def __init__(self,x,y,mov_speed, attack_speed ):
        self.range = 1
        self.x = x
        self.y = y
        self.avatar_move = True
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
        self.shootList = []

    def draw(self,screen):
        screen.blit(self.frame,self.rect)

    def shoot(self):
        self.shootList.append(Bullet(self.rect.centerx,self.rect.centery,self.damage,0))

    def draw_shoot(self,screen):
        for bullet in self.shootList: 
            bullet.direction()
            bullet.draw_bullet(screen,0)

  
class Avatar_lumberjack():  #3
    def __init__(self,x,y,mov_speed, attack_speed ):
        self.range = 2
        self.x = x
        self.y = y
        self.avatar_move = True
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
        self.range = 2
        self.x = x
        self.y = y
        self.avatar_move = True
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


class Bullet:
    def __init__(self,x,y,damage):
        self.damage = damage
        self.imagenA = pg.image.load(os.path.join(c.PATH,"bullets","SandRook.png"))
        self.rect = self.imagenA.get_rect()
        self.rect.centerx = x
        self.rect.centery = y-6
        self.speed = 5

    def direction(self):
        self.rect.centery -= self.speed
        

    def draw_bullet(self,screen):
        screen.blit(self.imagenA,self.rect)
class Bullet:
    def __init__(self,x,y,damage,i):
        self.damage = damage
        self.imagenA = pg.image.load(os.path.join(c.PATH,"bullets","TankBullet01.png"))
        self.imagenB = pg.image.load(os.path.join(c.PATH,"bullets","ArcherBullet01.png"))
        self.image = [self.imagenA,self.imagenB]
        self.rect = self.image[i].get_rect()
        self.rect.centerx = x
        self.rect.centery = y-6
        self.speed = 5

    def direction(self):
        self.rect.centery -= self.speed

    def draw_bullet(self,screen,i):
        screen.blit(self.image[i],self.rect)











    

    
        