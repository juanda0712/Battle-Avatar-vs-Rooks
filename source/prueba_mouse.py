import pygame as pg
from . import constants as c


def getMapIndex(x, y):  #devuelve el indice del mouse en la matrix
    x -= 238
    y -= 11
    return (x // 65, y // 65)

def getMapGridPos(map_x, map_y):    #devuelve la posicion de las cuadriculas de la matrix
        return (map_x * 65 + 65//2 + c.OFFSET_X,
                map_y * 65 + 65//5 * 3 + c.OFFSET_Y)

def pos():
    x,y =pg.mouse.get_pos()
    map_x,map_y = getMapIndex(x,y)
    position = getMapGridPos(map_x,map_y)
    print('---------------------------------------------------------------------------')
    print(f'Mouse Pos:  {(x,y)}  Matrix Index:  {getMapIndex(x,y)}')
    print(f'Matrix Grid: {position}')
    