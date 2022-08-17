import pygame as pg
from StateMachine.StateMachine import StateMachine, State
import config

if __name__ == "__main__":
    pg.init()

    screen = pg.display.set_mode(config.size)

    background = pg.Surface(config.size)
    background = background.convert()
    background.fill((170, 238, 187))

    if pg.font:
        font = pg.font.SysFont('Arial', 64)
        text = font.render("Snek", True, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        background.blit(text, textpos)
    
    screen.blit(background, (0, 0))
    pg.display.flip()
    clock = pg.time.Clock()

    stateMachine = StateMachine(screen)

    keepGameRunning = True
    while keepGameRunning:
        #max 60 fps
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                keepGameRunning = False
            if event.type == pg.MOUSEBUTTONDOWN:
                stateMachine.setState(State.playState) 

        stateMachine.runState()

        pg.display.update()


    
    pg.quit()
