import pygame as pg
import logging
from .StateInterface import StateInterface, State
from config import *


class InitState(StateInterface):

    def __init__(self, screen):
        logging.info("init state init")
        self.screen = screen
        #max 60 fps
        clock = pg.time.Clock()
        clock.tick(60)

    def isState(self, currentState) -> bool:
        return currentState == State.initState

    def run(self):

        background = pg.Surface(size)
        background = background.convert()
        background.fill((170, 238, 187))

        if pg.font:
            font = pg.font.SysFont('Arial', 64)
            text = font.render("Snek", True, Color.black)
            textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
            background.blit(text, textpos)
        
        self.screen.blit(background, (0, 0))
        pg.display.flip()
        return State.choiceState