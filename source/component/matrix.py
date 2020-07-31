import pygame as pg
from .. import constants as c
import random


class Board():

    def __init__(self):
        
        self.map = [[0 for x in range(c.M_WIDTH)] for y in range(c.M_HEIGHT)]
        self.torres = []

    def showMap(self):
        return self.map

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

    def getGridType(self,x,y):
        map_x, map_y = self.getMapIndex(x, y)
        if self.isValid(map_x, map_y) and self.isMovable(map_x, map_y):
            self.map[map_y][map_x] = 1










