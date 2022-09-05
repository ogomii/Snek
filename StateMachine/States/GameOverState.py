import pygame as pg
from config import *
import logging
from ..StateInterface import StateInterface, State
from ..EventHandler.EventHandler import EventHandler
from Utils.MousePossitionCalculator import *
from Utils.PossitionCalculator import *

class GameOverState(StateInterface):

    def __init__(self,screen, eventHandler):
        logging.info("Game Over state init")
        self.screen = screen
        self.eventHandler = eventHandler
        self.font = pg.font.SysFont('Arial', 45)
        self.gameOverText = self.font.render('GAME OVER', True, Color.red)
        self.playAgainText = self.font.render('PLAY AGAIN', True, Color.fullBlue)
        self.backToMenuText = self.font.render('MENU', True, Color.fullBlue)

    def isState(self, currentState) -> bool:
        return currentState == State.gameOver

    
    def run(self):
        mousePosition = pg.mouse.get_pos()
        self.screen.blit(self.gameOverText, (width/2 - 90, height/3 + 10))
        self.drawPlayAgainButton(width, height, mousePosition)
        self.drawBackToMenuButton(width, height, mousePosition)
        self.eventHandler.setState(State.gameOver)
    

    def drawBackToMenuButton(self, width, height, mousePosition) -> None:
        if isMouseOnBackToMenuButton(mousePosition):
            pg.draw.rect(self.screen, Color.darkBlue, backToMenuButtonPossition())
        else:
            pg.draw.rect(self.screen, Color.lightBlue, backToMenuButtonPossition())
        self.screen.blit(self.backToMenuText, backToMenuTextPossition())


    def drawPlayAgainButton(self, width, height, mousePosition) -> None:
        if isMoustOnPlayAgainButton(mousePosition):
            pg.draw.rect(self.screen, Color.darkBlue, playAgainButtonPossiton())
        else:
            pg.draw.rect(self.screen, Color.lightBlue, playAgainButtonPossiton())
        self.screen.blit(self.playAgainText, playAgainTextPossition())