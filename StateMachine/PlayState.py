import logging
from .StateInterface import StateInterface, State
from GameBoard.GameBoard import GameBoard

class PlayState(StateInterface):

    def __init__(self,screen):
        logging.info("play state init")
        self.screen = screen
        self.board = GameBoard(self.screen)
        self.board.placeSnakePart(4,0)
        self.board.placeApple()

    def isState(self, currentState) -> bool:
        return currentState == State.playState
    
    def run(self):
        self.screen.fill((0,0,0))
        self.board.update()
        return State.playState