import pygame as pg
import logging
from config import *
from ..StateInterface import StateInterface, State
from ..EventHandler.EventHandler import EventHandler
from MousePossitionCalculator import *

class ChoiceState(StateInterface):

    def __init__(self, screen, eventHandler):
        logging.info("choice state init")
        self.screen = screen
        self.eventHandler = eventHandler
        self.font = pg.font.SysFont('Arial', 55)
        self.button2Text = self.font.render('PLAY', True, Color.fullBlue)
        self.button1Text = self.font.render('HCA', True, Color.fullBlue)

    def isState(self, currentState) -> bool:
        return currentState == State.choiceState
    
    def run(self):
        mousePosition = pg.mouse.get_pos()
        self.drawHamiltonButton(width, height, mousePosition)
        self.drawPlayButton(width, height, mousePosition)
        self.eventHandler.setState(State.choiceState)

    def drawHamiltonButton(self, width, height, mousePosition) -> None:
        if isMouseOnHamiltonButton(mousePosition):
            pg.draw.rect(self.screen, Color.darkBlue, [width/2 - 280, height/2, 240, 80])
        else:
            pg.draw.rect(self.screen, Color.lightBlue, [width/2 - 280, height/2, 240, 80])
        self.screen.blit(self.button1Text, (width/2 - 210, height/2))


    def drawPlayButton(self, width, height, mousePosition):
        if isMouseOnPlayButton(mousePosition):
            pg.draw.rect(self.screen, Color.darkBlue, [width/2 + 40, height/2, 240, 80])
        else:
            pg.draw.rect(self.screen, Color.lightBlue, [width/2 + 40, height/2, 240, 80])
        self.screen.blit(self.button2Text, (width/2 + 100, height/2))