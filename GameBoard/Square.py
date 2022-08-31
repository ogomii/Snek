from genericpath import isfile
import pygame as pg
from config import *

class Square:

    def __init__(self, screen, posX, posY):
        self.screen = screen
        self.posX = posX
        self.posY = posY
        self.appleOnSquare = False
        self.snakeOnSquare = False
    
    def update(self):
        if self.appleOnSquare:
            self.drawApple()
        elif self.snakeOnSquare:
            self.drawSnakePart()
        return  
    
    def putSnakePart(self):
        self.snakeOnSquare = True
        self.appleOnSquare = False
    
    def putApple(self):
        self.appleOnSquare = True
        self.snakeOnSquare = False
    
    def deleteObjectsOnSquare(self):
        self.snakeOnSquare = False
        self.appleOnSquare = False

    def drawSnakePart(self):
        pg.draw.rect(self.screen, Color.green, [self.posX, self.posY, 40, 40])
    
    def drawApple(self):
        pg.draw.rect(self.screen, Color.red, [self.posX + 10, self.posY + 10, 20, 20])

    def clearSquare(self):
        pg.draw.rect(self.screen, Color.black, [self.posX, self.posY, 40, 40])
    
    def getPos(self):
        return (self.posX, self.posY)
    
    def isFree(self):
        return not self.isFilled()
    
    def isFilled(self):
        return self.appleOnSquare or self.snakeOnSquare