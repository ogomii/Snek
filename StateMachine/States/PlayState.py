import logging
from ..StateInterface import StateInterface, State
from GameBoard.GameBoard import GameBoard
from ..EventHandler.EventHandler import EventHandler
from config import *
from Timer import Timer

class PlayState(StateInterface):

    def __init__(self,screen, eventHandler):
        logging.info("play state init")
        self.screen = screen
        self.eventHandler = eventHandler
        self.board = GameBoard(self.screen)
        self.timer = Timer(TimeSettings.snakeMove)
        self.timer.start()


    def isState(self, currentState) -> bool:
        return currentState == State.playState
    

    def run(self):
        self.eventHandler.setState(State.playState)
        if self.timer.timeElapsed():
            self.setUpNextFrame()
            self.board.updateScreen()


    def setUpNextFrame(self):
        self.screen.fill((0,0,0))
        try:
            self.board.moveSnake(self.eventHandler.getLastDirectionalKey())
        except SnakeAteItself:
            self.eventHandler.setState(State.gameOver)
        