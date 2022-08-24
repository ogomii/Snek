from config import *
from .Square import Square

class GameBoard:

    def __init__(self, screen):
        self.screen = screen
        self.board = [[ Square(self.screen, xCoordinate * 40, yCoordiante * 40) for xCoordinate in range(int(squaresX))] for yCoordiante in range(int(squaresY))]
    
    def fill(self, posX, posY):
        self.board[posX][posY].fill()