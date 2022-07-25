import pygame as pg
from MouseActions import MouseActions


if __name__ == "__main__":
    pg.init()
    size = width, height = 1280, 720

    screen = pg.display.set_mode(size)

    background = pg.Surface(size)
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

    mouse = MouseActions()

    keepGameRunning = True
    while keepGameRunning:
        #max 60 fps
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                keepGameRunning = False

        mousePosition = pg.mouse.get_pos()
        mouse.drawButton1(screen, width, height, mousePosition)
        mouse.drawButton2(screen, width, height, mousePosition)
        
        pg.display.update()


    
    pg.quit()
