from .StateInterface import State
from .ChoiceState import ChoiceState
from .PlayState import PlayState

class StateMachine:


    def __init__(self, screen):
        self.currentState = State.choiceState
        self.screen = screen

    def runState(self):
        if self.currentState == State.choiceState:
           self.currentState = ChoiceState(self.screen) 
        elif self.currentState == State.playState:
            self.currentState = PlayState(self.screen)
        self.currentState.run()
    
    def setState(self, newState):
        self.currentState = newState