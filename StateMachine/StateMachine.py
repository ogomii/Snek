import pygame as pg
from config import *
from .StateInterface import State, StateInterface
from .ChoiceState import ChoiceState
from .PlayState import PlayState
from .InitState import InitState
from .HamiltonState import HamiltonSate

class StateMachine:


    def __init__(self):
        screen = pg.display.set_mode(size)
        self.StateObjects = []
        for stateClass in StateInterface.__subclasses__():
            self.StateObjects.append(stateClass(screen))
        self.currentState = State.initState
        self.runState()

    def runState(self):
        self.currentState = self.__getStateToRun().run()
    
    def setState(self, newState):
        self.currentState = newState

    def __getStateToRun(self):
        stateToRun = None
        for stateObject in self.StateObjects:
            if stateObject.isState(self.currentState):
                stateToRun = stateObject
                break
        return stateToRun
