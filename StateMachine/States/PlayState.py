import logging
from ..StateInterface import StateInterface, State
from GameBoard.GameBoard import GameBoard
from config import *
from Timer import Timer

class PlayState(StateInterface):

    def __init__(self,screen):
        logging.info("play state init")
        self.screen = screen
        self.board = GameBoard(self.screen)
        self.board.placeSnakePart(squaresY//2, squaresX//2)
        self.board.placeApple()
        self.timer = Timer(TimeSettings.snakeMove)
        self.timer.start()

    def isState(self, currentState) -> bool:
        return currentState == State.playState
    
    def run(self):
        self.screen.fill((0,0,0))
        self.setUpNextFrame()
        self.board.update()
        return State.playState

    def setUpNextFrame(self):
        if self.timer.timeElapsed():
            self.board.moveSnake()
        