import pygame as pg
from config import *

class Square:

    def __init__(self, screen, posX, posY):
        self.screen = screen
        self.posX = posX
        self.posY = posY
        self.filled = False
    
    def fill(self):
        pg.draw.rect(self.screen, Color.green, [self.posX, self.posY, 40, 40])
        self.filled = True

    def clear(self):
        pg.draw.rect(self.screen, Color.black, [self.posX, self.posY, 40, 40])
        self.filled = False
    
    def getPos(self):
        return (self.posX, self.posY)
    
    def isFilled(self):
        return self.filled