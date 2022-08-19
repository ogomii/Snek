from asyncio import current_task
from threading import currentThread
import pygame as pg
from config import *
from .StateInterface import State, StateInterface
from .ChoiceState import ChoiceState
from .PlayState import PlayState
from .InitState import InitState
from .HamiltonState import HamiltonSate
from MousePossitionCalculator import *

class StateMachine:


    def __init__(self):
        screen = pg.display.set_mode(size)

        self.StateObjects = []
        for stateClass in StateInterface.__subclasses__():
            self.StateObjects.append(stateClass(screen))

        self.currentState = State.initState
        self.runState()

    def runState(self):
        stateToRun = None

        for stateObject in self.StateObjects:
            if stateObject.isState(self.currentState):
                stateToRun = stateObject
                break

        self.currentState = stateToRun.run()
    
    def setState(self, newState):
        self.currentState = newState
    
    def setStateHamiltonOrPlay(self):
        mousePosition = pg.mouse.get_pos()
        if isMouseOnHamiltonButton(mousePosition):
            self.setState(State.hamiltonState)
        elif isMouseOnPlayButton(mousePosition):
            self.setState(State.playState) 
