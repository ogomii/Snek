from random import random
from config import *
from .Square import Square
import random

class GameBoard:

    def __init__(self, screen):
        self.screen = screen
        self.board = [[ Square(self.screen, xCoordinate * 40, yCoordiante * 40) for xCoordinate in range(int(squaresX))] for yCoordiante in range(int(squaresY))]
        self.snakeHeadPosition = [0,0]
    
    def placeSnakePart(self, posY, posX):
        if self.board[int(posY)][int(posX)].isFree():
            self.snakeHeadPosition = [posY, posX]
            self.board[int(posY)][int(posX)].drawSnakePart()

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
                if self.board[i][j].isFree():
                    emptySquares.append((i,j))
        return emptySquares
    
    def moveSnake(self):
        self.board[int(self.snakeHeadPosition[0])][int(self.snakeHeadPosition[1])].clearSquare()
        self.snakeHeadPosition[1] += 1
        if self.snakeHeadPosition[1] == squaresX:
            self.snakeHeadPosition[1] = 0
        self.board[int(self.snakeHeadPosition[0])][int(self.snakeHeadPosition[1])].drawSnakePart()
