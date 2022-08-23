import pygame as pg
from StateMachine.StateMachine import StateMachine, State
from MousePossitionCalculator import *

class EventHandler:
    
    def __init__(self, stateMachine):
        self.stateMachine = stateMachine
        pass

    def handleEvents(self):
        keepGameRunning = True
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                keepGameRunning = False
            if event.type == pg.MOUSEBUTTONDOWN:
                self.setStateHamiltonOrPlay()

        return keepGameRunning
    
    def setStateHamiltonOrPlay(self):
        mousePosition = pg.mouse.get_pos()
        if isMouseOnHamiltonButton(mousePosition):
            self.stateMachine.setState(State.hamiltonState)
        elif isMouseOnPlayButton(mousePosition):
            self.stateMachine.setState(State.playState) 