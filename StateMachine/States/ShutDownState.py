import logging
from ..StateInterface import StateInterface, State

class ShutDownState(StateInterface):

    def __init__(self, screen):
        logging.info("shut down state init")
        self.screen = screen

    def run(self):
        self.screen.fill((0,0,0))
        return State.shutDown

    def isState(self, currentState) -> bool:
        return currentState == State.shutDown