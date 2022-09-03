import pygame as pg
from config import *
import logging
from ..StateInterface import StateInterface, State
from ..EventHandler.EventHandler import EventHandler

class GameOverState(StateInterface):

    def __init__(self,screen, eventHandler):
        logging.info("Game Over state init")
        self.screen = screen
        self.eventHandler = eventHandler

    def isState(self, currentState) -> bool:
        return currentState == State.gameOver
    
    def run(self):
        self.eventHandler.setState(State.shutDown)