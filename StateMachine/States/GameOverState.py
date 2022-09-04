import pygame as pg
from config import *
import logging
from ..StateInterface import StateInterface, State
from ..EventHandler.EventHandler import EventHandler
from MousePossitionCalculator import *

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
            pg.draw.rect(self.screen, Color.darkBlue, [width/2 - 280, height/3 * 2, 240, 80])
        else:
            pg.draw.rect(self.screen, Color.lightBlue, [width/2 - 280, height/3 * 2, 240, 80])
        self.screen.blit(self.backToMenuText, (width/2 - 210, height/3 * 2 + 10))


    def drawPlayAgainButton(self, width, height, mousePosition) -> None:
        if isMoustOnPlayAgainButton(mousePosition):
            pg.draw.rect(self.screen, Color.darkBlue, [width/2 + 40, height/3 * 2, 240, 80])
        else:
            pg.draw.rect(self.screen, Color.lightBlue, [width/2 + 40, height/3 * 2, 240, 80])
        self.screen.blit(self.playAgainText, (width/2 + 60, height/3 * 2 + 10))