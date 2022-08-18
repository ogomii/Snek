import pygame as pg
from config import *
from .StateInterface import State
from .ChoiceState import ChoiceState
from .PlayState import PlayState
from .InitState import InitState
from .HamiltonState import HamiltonSate
from MousePossitionCalculator import *

class StateMachine:


    def __init__(self):
        screen = pg.display.set_mode(size)
        self.currentState = State.initState
        self.initState = InitState(screen)
        self.choiceState = ChoiceState(screen)
        self.playState = PlayState(screen)
        self.hamiltonState = HamiltonSate(screen)
        self.runState()

    def runState(self):
        stateToRun = None

        if self.currentState == State.initState:
            stateToRun = self.initState
        elif self.currentState == State.choiceState:
           stateToRun = self.choiceState 
        elif self.currentState == State.playState:
            stateToRun = self.playState
        elif self.currentState == State.hamiltonState:
            stateToRun = self.hamiltonState

        self.currentState = stateToRun.run()
    
    def setState(self, newState):
        self.currentState = newState
    
    def setStateHamiltonOrPlay(self):
        mousePosition = pg.mouse.get_pos()
        if isMouseOnHamiltonButton(mousePosition):
            self.setState(State.hamiltonState)
        elif isMouseOnPlayButton(mousePosition):
            self.setState(State.playState) 
