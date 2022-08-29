import logging
from ..StateInterface import StateInterface, State
from ..EventHandler.EventHandler import EventHandler

class ShutDownState(StateInterface):

    def __init__(self, screen, eventHandler):
        logging.info("shut down state init")
        self.screen = screen
        self.eventHandler = eventHandler

    def run(self):
        self.screen.fill((0,0,0))
        self.eventHandler.setState(State.shutDown)

    def isState(self, currentState) -> bool:
        return currentState == State.shutDown