import pygame as pg
from config import *
from StateMachine.StateMachine import StateMachine, State


if __name__ == "__main__":

    pg.init()
    stateMachine = StateMachine()

    while stateMachine.getState() != State.shutDown:

        stateMachine.handleEvents()
        stateMachine.runState()

        pg.display.update()


    pg.quit()

