import pygame as pg
from config import *
import logging
from ..StateInterface import StateInterface, State
from ..EventHandler.EventHandler import EventHandler
from GameBoard.GameBoard import GameBoard

class HamiltonSate(StateInterface):

    def __init__(self,screen, eventHandler):
        logging.info("hamilton state init")
        self.screen = screen
        self.eventHandler = eventHandler
        self.board = GameBoard(self.screen)

    def isState(self, currentState) -> bool:
        return currentState == State.hamiltonState
    
    def run(self):
        self.screen.fill((0,0,0))
        self.board.fill(0,0)
        self.eventHandler.setState(State.hamiltonState)