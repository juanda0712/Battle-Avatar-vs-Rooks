import pygame as pg

ORIGINAL_TITLE   = 'BATTLE'
ORIGINAL_CAPTION = 'Avatars vs Rooks'


PATH = "C:/Users/JuanDa/Documents/I SEMESTRE 2020/CURSOS CARRERA/Battle Avatars vs Rooks/Battle-Avatar-vs-Rooks/source/component/images"
PATH2 = "C:/Users/JuanDa/Documents/I SEMESTRE 2020/CURSOS CARRERA/Battle Avatars vs Rooks/Battle-Avatar-vs-Rooks/source/component/images"
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 680
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)

WHITE        = (255, 255, 255)
NAVYBLUE     = ( 60,  60, 100)
SKY_BLUE     = ( 39, 145, 251)
BLACK        = (  0,   0,   0)
LIGHTYELLOW  = (234, 233, 171)
RED          = (255,   0,   0)
PURPLE       = (255,   0, 255)
GOLD         = (255, 215,   0)
GREEN        = (0, 255,   0)
BROWN        = (102, 51, 0)
LIGHTBROWN   = (191, 113,  35)
TRANS        = (38, 25, 2 )

#Title principal screen
FONT_SIZE = 65

#buttons position
X  = 340
Y  = 160
X1 = 150
Y1 = 30


#Names Buttons
NG  = "New game"
LG  = "Load game"
CON = "Configuration"
HOF = "Hall of fame"
CR  = "Credits"
HE  = "Help"
EX  = "Exit"


#GAME BUTTONS
SR = "Sand Rook"
RR = "Rock Rook"
FR = "Fire Rook"
WR = "Water Rook"
X_GAME = 80
Y_GAME = 100


#matrix constants
M_WIDTH   = 5
M_HEIGHT  = 9
DIMENTION = 65
M = []
MAP_EMPTY = 0
MAP_EXIST = 1

OFFSET_X = 238
OFFSET_Y = 11

F_BULLET = 596

#Timer constants
X_TIMER  = 575
Y_TIMER  = 150
TIME_POS = (X_TIMER,Y_TIMER)
FONT_SIZE_TIMER = 22

#player name constants
X_NAME   = 575
Y_NAME   = 100
NAME_POS = (X_NAME,Y_NAME)


#state
FLY = 'fly'



#avatars
WALK = 'walk'
ATTACK = 'attack'
DIE = 'die'



    #types
TANK = 'tank'
LUMBERJACK = 'lumberjack'
CANNIBAL = 'cannibal'
ARCHER = 'archer'