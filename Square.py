from config import *
import pygame as pg

class Square:

    def __init__(self, screen, posX, posY):
        self.screen = screen
        self.posX = posX
        self.posY = posY
    
    def fill(self):
        pg.draw.rect(self.screen, Color.green, [self.posX, self.posY, 40, 40])