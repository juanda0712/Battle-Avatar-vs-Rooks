import random
import pygame as pg
from .. import tool
from .. import constants as c

class Bullet(pg.sprite.Sprite):
    def __init__(self, y, start_x, dest_x, name, damage, sand, rock, fire, water):
        pg.sprite.Sprite.__init__(self)

        self.name = name
        self.frames = []
        self.frame_index = 0
        self.load_images()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = start_x
        self.dest_x = dest_x
        self.x_vel = 4 if (dest_x > start_x) else -4
        self.y_vel = 4
        self.damage = damage
        self.sand = sand
        self.rock = rock
        self.fire = fire
        self.water = water
        self.state = c.FLY
        self.current_time = 0

    def loadFrames(self, frames, name):
        frame_list = tool.GFX[name]
        if name in tool.ROOK_RECT:
            data = tool.ROOK_RECT[name]
            x = data['x']
            y = data['y']
            width = ['width']
            height = ['height']
        else:
            x = 0
            y = 0
            rect = frame_list[0].get_rect()
            width = rect.w
            height = rect.h

        for frame in frame_list:
            frames.append(tool.get_image(frame, x, y, width, height))

    def load_images(self):
        self.fly_frames ==  []

        fly_name = self.name 
        self.loadFrames(self.fly_frames, fly_name)

        self.frames = self.fly_frames
        
    def uptade(self, game_info):
        self.current_time = game_info[c.CURRENT_TIME]
        if self.state == c.FLY:
            if self.rect.x != self.dest_x:
                self.rect.x += self.x_vel
                if self.x_vel * (self.dest_x - self.rect.x) < 0:
                    self.rect.x = self.dest_x
            self.rect.y += self.y_vel
            if self.rect.y > c.SCREEN_HEIGHT:
                self.kill()
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
                

class Rook(pg.sprite.Sprite):
    def __init__(self, x, y, health, bullet_group, scale = 1):
        pg.sprite.Sprite.__init__(self)

        self.frames = []
        self.frame_index = 0
        self.load_images(name, scale)
        self.frame_num = len(self.frames)
        self.image = self.frames[self.frame_index]
        self.rect = self.image
        self.rect.contrex = x
        self.rect.bottom = y
        self.name = name
        self.health = health
        self.state = c.IDLE
        self.bullet_group = bullet_group
        self.animate_timer = 0
        self.animate_interval = 100
        self.hit_timer = 0

    def loadFrames(self, frames, name, scale, color = c.BLACK):
        frame_list = tool.GFX[name]
        if name in tool.ROOK_RECT:
            data = tool.ROOK_RECT[name]
            x = data['x']
            y = data['y']
            width = data['width']
            height = data['height']
        else:
            x = 0
            y = 0
            rect = frame_list[0].get_rect()
            width = rect.w
            height = rect.h

        for frame in frame_list:
            frames.append(tool.get_image(frame, x, y, width, height, color, scale))

    def loadImage(self, name, scale):
        self.loadFrames(self.frames, name, scale)

    def changeFrames(self, frames):
        self.frames = frames
        self.frame_num = len(self.frames)
        self.frame_index = 0

        bottom = self.frames[self.frame_index]
        x = self.rect.x
        self.image = self.frames[self.frame_index]
        self.rect = self.image,get_rect
        self.rect.bottom = bottom
        self.rect.x = x

    def update(self, game_info):
        self.current_time = game_info[c.CURRENT_TIME]
        #self.handleState()
        self.animation()

    def handleState(self):
        if self.state == c.IDLE:
            self.idling()
        elif self.state == c.ATTACK:
            self.attacking()
        
    def idling(self):
        pass

    def attacking(self):
        pass 

    def animation(self):
        if (self.current_time - self.animate_timer) > self.animate_interval:
            self.frame_index += 1
            if self.frame_index >= self.frame_num:
                self.frame_index = 0
            self.animate_timer = self.current_time
        self.image = self.frames[self.frame_index]
        if (self.current_time - self.hit_timer) >= 200:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(192)

    def setAttack(self):
        self.state = c.ATTACK
    
    def setIdle(self):
        self.state = c.IDLE
        self.is_attacked = False

    def setDamage(self, damage, avatar):
        self.health -= damage
        self.hit_timer = self.current_time
        if self.health <= 0:
            self.kill_avatar = avatar 

    def getPosition(self):
        return self.rect.centerx, self.rect.bottom

class SandRook(Rook):
     def __init__(self, x, y, bullet_group):
        Rook.__init__(slef, x, y, c.SANDROOK, c.ROOK_HEALTH, bullet_group)
        self.shoot_timer = 0 

    def attacking(self):
        if (self.current_time - self.shoot_timer) > 2000:
            self.bullet_group.add(Bullet('self.rect.right', self.rect.y, self.rect.y, c.BULLET_SAND, c.BULLET_DAMAGE_NORMAL, True, False, False, False))
            self.shoot_timer = self.current_time

class RockRook(Rook):
    def __init__(self, x, y, bullet_group):
        Rook.__init__(slef, x, y, c.ROCKROOK, c.ROOK_HEALTH, bullet_group)
        self.shoot_timer = 0 

    def attacking(self):
        if (self.current_time - self.shoot_timer) > 2000:
            self.bullet_group.add(Bullet('self.rect.right', self.rect.y, self.rect.y, c.BULLET_ROCK, c.BULLET_DAMAGE_NORMAL, False, True, False, False))
            self.shoot_timer = self.current_time

class FireRook(Rook):
    def __init__(self, x, y, bullet_group):
        Rook.__init__(slef, x, y, c.FIREROOK, c.ROOK_HEALTH, bullet_group)
        self.shoot_timer = 0 

    def attacking(self):
        if (self.current_time - self.shoot_timer) > 2000:
            self.bullet_group.add(Bullet('self.rect.right', self.rect.y, self.rect.y, c.BULLET_FIRE, c.BULLET_DAMAGE_NORMAL, False, False, True, False))
            self.shoot_timer = self.current_time

class WaterRook(Rook):
    def __init__(self, x, y, bullet_group):
        Rook.__init__(slef, x, y, c.WATERROOK, c.ROOK_HEALTH, bullet_group)
        self.shoot_timer = 0 

    def attacking(self):
        if (self.current_time - self.shoot_timer) > 2000:
            self.bullet_group.add(Bullet('self.rect.right', self.rect.y, self.rect.y, c.BULLET_WATER, c.BULLET_DAMAGE_NORMAL, False, False, False, True))
            self.shoot_timer = self.current_time