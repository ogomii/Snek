from random import random
from config import *
from .Square import Square
from .SnakeBody import SnakeBody
import random

class GameBoard:

    def __init__(self, screen):
        self.screen = screen
        self.board = [[ Square(self.screen, xCoordinate * 40, yCoordiante * 40) for xCoordinate in range(int(squaresX))] for yCoordiante in range(int(squaresY))]
        self.snakeBody = []
        self.moveSnakeDirection = MoveDirection.right
        self.placeSnakePart(squaresY//2, squaresX//2)
        self.eatenApplesCounter = 0
        self.appleEaten = False
        self.placeApple()

    
    def placeSnakePart(self, posY, posX):
        if self.board[int(posY)][int(posX)].isFree():
            self.snakeBody.append(SnakeBody(posY, posX, self.moveSnakeDirection))
            self.board[int(posY)][int(posX)].putSnakePart()


    def updateScreen(self):
        if self.appleEaten:
            self.placeApple()
            self.appleEaten = False
        for i in range(int(squaresY)):
            for j in range(int(squaresX)):
                self.board[i][j].update()

    
    def placeApple(self):
        emptySquares = self.gatherEmptySquares()
        if len(emptySquares) != 0:
            chosenSquare = random.randint(0, len(emptySquares))
            self.board[emptySquares[chosenSquare][0]][emptySquares[chosenSquare][1]].putApple()

    
    def gatherEmptySquares(self):
        emptySquares = []
        for i in range(int(squaresY)):
            for j in range(int(squaresX)):
                if self.board[i][j].isFree():
                    emptySquares.append((i,j))
        return emptySquares

    
    def moveSnake(self, moveSnakeDirection):
        self.moveSnakeDirection = moveSnakeDirection
        if self._snakeWillEatItself():
            raise SnakeAteItself

        self._clearSnakeFromBoard()
        self._updateSnakePosition()
        if self.board[int(self.snakeBody[0].posY)][int(self.snakeBody[0].posX)].isAppleOnSquare():
            self._eatApple()
        self._putSnakePartsOnBoard()
    

    def _clearSnakeFromBoard(self):
        for snakePartIndex in range(len(self.snakeBody)):
            self.board[int(self.snakeBody[snakePartIndex].posY)][int(self.snakeBody[snakePartIndex].posX)].deleteObjectsOnSquare()
    

    def _putSnakePartsOnBoard(self):
        for snakePartIndex in range(len(self.snakeBody)):
            self.board[int(self.snakeBody[snakePartIndex].posY)][int(self.snakeBody[snakePartIndex].posX)].putSnakePart()
    
    
    def _eatApple(self):
        self.appleEaten = True
        self.eatenApplesCounter += 1
        snakeTail = self.snakeBody[-1]
        self.snakeBody.append(SnakeBody(snakeTail.posY, snakeTail.posX, MoveDirection.none))

    
    def _updateSnakePosition(self):
        self._moveEveryPart()
        self._updateSnakePartsMovingDirection()

    def _moveEveryPart(self):
        for snakePartIndex in range(len(self.snakeBody)):
            self._movePart(self.snakeBody[snakePartIndex])

    
    def _movePart(self, snakePart):
        if snakePart.movingDirection == MoveDirection.right:
            self._updateSnakePartPosition(snakePart, 0, 1)
        elif snakePart.movingDirection == MoveDirection.left:
            self._updateSnakePartPosition(snakePart, 0, -1)
        elif snakePart.movingDirection == MoveDirection.up:
            self._updateSnakePartPosition(snakePart, -1, 0)
        elif snakePart.movingDirection == MoveDirection.down:
            self._updateSnakePartPosition(snakePart, 1, 0)
        elif snakePart.movingDirection == MoveDirection.none:
            pass


    def _updateSnakePartsMovingDirection(self):
        newMoveSnakeDirection = self.moveSnakeDirection
        for snakePartIndex in range(len(self.snakeBody)):
            snakeDirectionForNextPart = self.snakeBody[snakePartIndex].movingDirection
            self.snakeBody[snakePartIndex].movingDirection = newMoveSnakeDirection
            newMoveSnakeDirection = snakeDirectionForNextPart


    def _updateSnakePartPosition(self, snakePart, yAxis, xAxis):
        snakePart.posY += yAxis
        if snakePart.posY== squaresY:
            snakePart.posY = 0
        elif snakePart.posY == -1:
            snakePart.posY = squaresY - 1
        snakePart.posX += xAxis
        if snakePart.posX == squaresX:
            snakePart.posX = 0
        elif snakePart.posX == -1:
            snakePart.posX = squaresX - 1
        
    def _snakeWillEatItself(self):
        dummyHead = SnakeBody(self.snakeBody[0].posY, self.snakeBody[0].posX, self.snakeBody[0].movingDirection)
        self._movePart(dummyHead)
        if self.board[int(dummyHead.posY)][int(dummyHead.posX)].isSnakeOnSquare():
            return True
        return False

