import pygame as pg
from config import *
from .StateInterface import State, StateInterface
from .States.ChoiceState import ChoiceState
from .States.PlayState import PlayState
from .States.InitState import InitState
from .States.HamiltonState import HamiltonSate
from .States.ShutDownState import ShutDownState
from .EventHandler.EventHandler import EventHandler
from .States.GameOverState import GameOverState

class StateMachine:


    def __init__(self):
        screen = pg.display.set_mode(size)
        self.StateObjects = []
        self.eventHandler = EventHandler()
        self.currentState = self.eventHandler.getState()
        for stateClass in StateInterface.__subclasses__():
            self.StateObjects.append(stateClass(screen, self.eventHandler))
    
    def handleEvents(self):
        self.eventHandler.handleEvents()
        self.currentState = self.eventHandler.getState()

    def runState(self):
        self._getStateObjectToRun().run()

    def getState(self):
        return self.currentState

    def _getStateObjectToRun(self):
        stateToRun = None
        for stateObject in self.StateObjects:
            if stateObject.isState(self.currentState):
                stateToRun = stateObject
                break
        return stateToRun
