import pygame as pg
from config import *
import logging
from .StateInterface import StateInterface, State
from Square import Square

class HamiltonSate(StateInterface):

    def __init__(self,screen):
        logging.info("hamilton state init")
        self.screen = screen
        self.board = [[0]*int(squaresX)]*int(squaresY)

    def isState(self, currentState) -> bool:
        return currentState == State.hamiltonState
    
    def run(self):
        self.screen.fill((0,0,0))
        self.board[0][0] = Square(self.screen, 0, 0)
        self.board[0][0].fill()
        return State.hamiltonState