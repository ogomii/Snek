from random import random
from config import *
from .Square import Square
import random

class GameBoard:

    def __init__(self, screen):
        self.screen = screen
        self.board = [[ Square(self.screen, xCoordinate * 40, yCoordiante * 40) for xCoordinate in range(int(squaresX))] for yCoordiante in range(int(squaresY))]
    
    def placeSnakePart(self, posX, posY):
        self.board[posX][posY].drawSnakePart()

    def update(self):
        for i in range(int(squaresY)):
            for j in range(int(squaresX)):
                self.board[i][j].update()
    
    def placeApple(self):
        emptySquares = self.gatherEmptySquares()
        if len(emptySquares) != 0:
            chosenSquare = random.randint(0, len(emptySquares))
            self.board[emptySquares[chosenSquare][0]][emptySquares[chosenSquare][1]].drawApple()
    
    def gatherEmptySquares(self):
        emptySquares = []
        for i in range(int(squaresY)):
            for j in range(int(squaresX)):
                if self.board[i][j].isFilled() == False:
                    emptySquares.append((i,j))
        return emptySquares