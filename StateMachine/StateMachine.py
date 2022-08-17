import pygame as pg
from config import *
from .StateInterface import State
from .ChoiceState import ChoiceState
from .PlayState import PlayState
from .InitState import InitState

class StateMachine:


    def __init__(self):
        screen = pg.display.set_mode(size)
        self.currentState = State.initState
        self.initState = InitState(screen)
        self.choiceState = ChoiceState(screen)
        self.playState = PlayState(screen)
        self.runState()

    def runState(self):
        stateToRun = None

        if self.currentState == State.initState:
            stateToRun = self.initState
        elif self.currentState == State.choiceState:
           stateToRun = self.choiceState 
        elif self.currentState == State.playState:
            stateToRun = self.playState

        self.currentState = stateToRun.run()
    
    def setState(self, newState):
        self.currentState = newState