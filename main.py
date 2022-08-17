import pygame as pg
from StateMachine.StateMachine import StateMachine, State
import config

if __name__ == "__main__":

    pg.init()
    stateMachine = StateMachine()

    keepGameRunning = True
    while keepGameRunning:

        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                keepGameRunning = False
            if event.type == pg.MOUSEBUTTONDOWN:
                stateMachine.setState(State.playState) 

        stateMachine.runState()

        pg.display.update()


    
    pg.quit()
