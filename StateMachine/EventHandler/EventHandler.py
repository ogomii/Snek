from asyncio import ReadTransport
import pygame as pg
from ..StateInterface import State
from MousePossitionCalculator import *

directionalKeys = {
    pg.K_RIGHT: MoveDirection.right,
    pg.K_LEFT : MoveDirection.left,
    pg.K_DOWN : MoveDirection.down,
    pg.K_UP   : MoveDirection.up
}

class EventHandler:
    
    def __init__(self):
        self.currentState = State.initState
        self.lastDirectionalKey = MoveDirection.right

    
    def setState(self, newState):
        self.currentState = newState
    

    def getLastDirectionalKey(self):
        return self.lastDirectionalKey

    
    def getState(self):
        return self.currentState

    
    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.currentState = State.shutDown
            if event.type == pg.MOUSEBUTTONDOWN:
                self.setNewState()
            if self.directionalKeysPressed(event):
                self.lastDirectionalKey = directionalKeys[event.key]

    
    def setNewState(self):
        mousePosition = pg.mouse.get_pos()
        if self.currentState == State.choiceState:
            if isMouseOnHamiltonButton(mousePosition):
                self.currentState = State.hamiltonState
            elif isMouseOnPlayButton(mousePosition):
                self.currentState = State.playState
        elif self.currentState == State.gameOver:
            if isMouseOnBackToMenuButton(mousePosition):
                self.currentState = State.initState
            elif isMoustOnPlayAgainButton(mousePosition):
                self.currentState = State.playState

    

    def directionalKeysPressed(self, event):
        if event.type == pg.KEYDOWN:
            return event.key == pg.K_UP or event.key == pg.K_DOWN or event.key == pg.K_RIGHT or event.key == pg.K_LEFT
        return False
