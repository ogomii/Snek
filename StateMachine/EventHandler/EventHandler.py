import pygame as pg
from ..StateInterface import State
from MousePossitionCalculator import *

class EventHandler:
    
    def __init__(self):
        self.currentState = State.initState

    def getState(self):
        return self.currentState
    
    def handleEvents(self, currentState):
        self.currentState = currentState
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.currentState = State.shutDown
            if event.type == pg.MOUSEBUTTONDOWN:
                self.setStateHamiltonOrPlay()
    
    def setStateHamiltonOrPlay(self):
        mousePosition = pg.mouse.get_pos()
        if isMouseOnHamiltonButton(mousePosition):
            self.currentState = State.hamiltonState
        elif isMouseOnPlayButton(mousePosition):
            self.currentState = State.playState