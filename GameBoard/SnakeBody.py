from config import *

class SnakeBody:

    def __init__(self, posY, posX, movingDirection: MoveDirection):
        self.posY = posY
        self.posX = posX
        self.movingDirection = movingDirection

    def getPosY(self):
        return int(self.posY)

    def getPosX(self):
        return int(self.posX)