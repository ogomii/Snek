from matplotlib.colors import LightSource
import pygame as pg

lightBlue = (50, 168, 166)
darkBlue = (50 ,131, 168)

class MouseActions:

    def __init__(self):
        self.font = pg.font.SysFont('Arial', 55)
        self.button2Text = self.font.render('PLAY', True, (0,0,120))
        self.button1Text = self.font.render('HCA', True, (0,0,120))

    def drawButton1(self, screen, width, height, mousePosition) -> None:
        if width/2 - 280 <= mousePosition[0] <= width/2 - 40 and height/2 <= mousePosition[1] <= height/2 + 80:
            pg.draw.rect(screen, darkBlue, [width/2 - 280, height/2, 240, 80])
        else:
            pg.draw.rect(screen, lightBlue, [width/2 - 280, height/2, 240, 80])
        screen.blit(self.button1Text, (width/2 - 210, height/2))


    def drawButton2(self, screen, width, height, mousePosition):
        if width/2 + 40 <= mousePosition[0] <= width/2 + 280 and height/2 <= mousePosition[1] <= height/2 + 80:
            pg.draw.rect(screen, darkBlue, [width/2 + 40, height/2, 240, 80])
        else:
            pg.draw.rect(screen, lightBlue, [width/2 + 40, height/2, 240, 80])
        screen.blit(self.button2Text, (width/2 + 100, height/2))