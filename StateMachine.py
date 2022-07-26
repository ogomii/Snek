from MouseActions import MouseActions
from Play import Play
from config import State


class StateMachine:


    def __init__(self, screen):
        self.currentState = State.chooseState
        self.mouse = MouseActions(screen)
        self.play = Play(screen)

    def runState(self):
        if self.currentState == State.chooseState:
           self.currentState = self.mouse.run() 
        elif self.currentState == State.playState:
            self.currentState = self.play.run()
    
    def setState(self, newState):
        self.currentState = newState