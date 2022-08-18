import pygame as pg
from StateMachine.StateMachine import StateMachine, State
from config import *


def eventsHandling(stateMachine):
    keepGameRunning = True
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            keepGameRunning = False
        if event.type == pg.MOUSEBUTTONDOWN:
            stateMachine.setStateHamiltonOrPlay()

    return keepGameRunning


if __name__ == "__main__":

    pg.init()
    stateMachine = StateMachine()

    keepGameRunning = True
    while keepGameRunning:

        keepGameRunning = eventsHandling(stateMachine)

        stateMachine.runState()

        pg.display.update()


    pg.quit()

