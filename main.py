import pygame as pg
from config import *
from StateMachine.StateMachine import StateMachine
from EventHandler.EventHandler import EventHandler


if __name__ == "__main__":

    pg.init()
    stateMachine = StateMachine()
    eventHandler = EventHandler(stateMachine)

    keepGameRunning = True
    while keepGameRunning:

        keepGameRunning = eventHandler.handleEvents()
        stateMachine.runState()

        pg.display.update()


    pg.quit()

