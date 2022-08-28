import pygame as pg
import logging
from config import *
from ..StateInterface import StateInterface, State
from MousePossitionCalculator import *

class ChoiceState(StateInterface):

    def __init__(self, screen):
        logging.info("choice state init")
        self.screen = screen
        self.font = pg.font.SysFont('Arial', 55)
        self.button2Text = self.font.render('PLAY', True, (0,0,120))
        self.button1Text = self.font.render('HCA', True, (0,0,120))

    def isState(self, currentState) -> bool:
        return currentState == State.choiceState
    
    def run(self):
        mousePosition = pg.mouse.get_pos()
        self.drawButton1(self.screen, width, height, mousePosition)
        self.drawButton2(self.screen, width, height, mousePosition)
        return State.choiceState                

    def drawButton1(self, screen, width, height, mousePosition) -> None:
        if isMouseOnHamiltonButton(mousePosition):
            pg.draw.rect(screen, Color.darkBlue, [width/2 - 280, height/2, 240, 80])
        else:
            pg.draw.rect(screen, Color.lightBlue, [width/2 - 280, height/2, 240, 80])
        screen.blit(self.button1Text, (width/2 - 210, height/2))


    def drawButton2(self, screen, width, height, mousePosition):
        if isMouseOnPlayButton(mousePosition):
            pg.draw.rect(screen, Color.darkBlue, [width/2 + 40, height/2, 240, 80])
        else:
            pg.draw.rect(screen, Color.lightBlue, [width/2 + 40, height/2, 240, 80])
        screen.blit(self.button2Text, (width/2 + 100, height/2))