import pygame as pg
from .. import constants as c
import random

class Torre(pg.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        pg.sprite.Sprite.__init__(self)
        self.torre = pg.image.load(r'C:\Users\JuanDa\Documents\I SEMESTRE 2020\CURSOS CARRERA\Battle Avatars vs Rooks\Battle-Avatar-vs-Rooks\source\component\1.png')
        self.rect = self.torre.get_rect()
        self.rect.centerx = pos_x
        self.rect.centery = pos_y-6
    
    def dibujar(self,superficie):
        superficie.blit(self.torre,self.rect)
        


class Board():

    def __init__(self,screen):
        self.screen = screen
        self.map = [[0 for x in range(c.M_WIDTH)] for y in range(c.M_HEIGHT)]
        self.torres = []

    def showMap(self):
        return self.map

    def create_board(self):
        count = 0
        for i in range(c.M_HEIGHT):
            for j in range(c.M_WIDTH):
                x,y = j*c.DIMENTION, i*c.DIMENTION
                if count%2 == 0:
                    pg.draw.rect(self.screen, c.BLACK, [x+c.OFFSET_X, y+c.OFFSET_Y, c.DIMENTION, c.DIMENTION], 0)
                    count +=1
                else:
                    pg.draw.rect(self.screen, c.RED, [x+c.OFFSET_X, y+c.OFFSET_Y, c.DIMENTION, c.DIMENTION], 0)
                    count +=1

    def detect(self):
        
        for n in range(c.M_HEIGHT):
            for m in range(c.M_WIDTH):
                if self.map[n][m] == 1:
                    map_x, map_y = self.getMapGridPos(m, n)
                    t = Torre(map_x, map_y)
                    t.dibujar(self.screen)
                
    

    def isValid(self, map_x, map_y):  #return True or False
        if (map_x < 0 or map_x >= c.M_WIDTH or
            map_y < 0 or map_y >= c.M_HEIGHT):
            return False
        return True

    def isMovable(self, map_x, map_y):   #return True si es 0  or False si es 1 osea (esta ocupado)
        return (self.map[map_y][map_x] == c.MAP_EMPTY)

    def getMapIndex(self,x, y):  #devuelve la cuadricula en la que esta el mouse
        x -= c.OFFSET_X
        y -= c.OFFSET_Y
        return (x // c.DIMENTION, y // c.DIMENTION)

    def getMapGridPos(self,map_x, map_y):    #devuelve la posicion de las cuadriculas de la matrix
        return (map_x * c.DIMENTION + c.DIMENTION//2 + c.OFFSET_X,
                map_y * c.DIMENTION + c.DIMENTION//5 * 3 + c.OFFSET_Y)

    
    def setMapGridType(self, map_x, map_y, type):  #Asigna un tipo a la cuadricula
        self.map[map_y][map_x] = type 

    
    def getRandomMapIndex(self):  #devuelve una posicion aleatoria de la matriz   
            map_x = random.randint(0, c.M_WIDTH-1)
            map_y = random.randint(0, c.M_HEIGHT-1)
            return (map_x, map_y)

    def showRooks(self, x, y):  
        pos = None
        map_x, map_y = self.getMapIndex(x, y)
        if self.isValid(map_x, map_y) and self.isMovable(map_x, map_y):
            pos = self.getMapGridPos(map_x, map_y)
        return pos

    def showGrid(self,x,y):
        map_x, map_y = self.getMapIndex(x, y)
        if self.isValid(map_x, map_y) and self.isMovable(map_x, map_y):
            self.map[map_y][map_x] = 1










