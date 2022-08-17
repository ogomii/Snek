from .StateInterface import StateInterface, State

class PlayState(StateInterface):

    def __init__(self,screen):
        self.screen = screen
    
    def run(self):
        self.screen.fill((0,0,0))
        return State.playState