
import logging
from .StateInterface import StateInterface, State

class HamiltonSate(StateInterface):

    def __init__(self,screen):
        logging.info("hamilton state init")
        self.screen = screen

    def isState(self, currentState) -> bool:
        return currentState == State.hamiltonState
    
    def run(self):
        self.screen.fill((0,0,0))
        return State.hamiltonState