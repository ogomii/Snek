from config import *

def isMouseOnHamiltonButton(mousePosition):
    if width/2 - 280 <= mousePosition[0] <= width/2 - 40 and height/2 <= mousePosition[1] <= height/2 + 80:
        return True
    else:
        return False


def isMouseOnPlayButton(mousePosition):
    if width/2 + 40 <= mousePosition[0] <= width/2 + 280 and height/2 <= mousePosition[1] <= height/2 + 80:
        return True
    else:
        return False
    

def isMoustOnPlayAgainButton(mousePosition):
    if width/2 + 40 <= mousePosition[0] <= width/2 + 280 and height/3 * 2 <= mousePosition[1] <= height/3 * 2 + 80:
        return True
    else:
        return False
    

def isMouseOnBackToMenuButton(mousePosition):
    if width/2 - 280 <= mousePosition[0] <= width/2 - 40 and height/3 * 2 <= mousePosition[1] <= height/3 * 2 + 80:
        return True
    else:
        return False