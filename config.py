import logging


logging.basicConfig(level = logging.INFO)

size = width, height = 1280, 720
squaresY: int = height / 40
squaresX: int = width / 40

class SnakeAteItself(Exception):
    pass

class TimeSettings:
    '''time to elapse in seconds'''
    snakeMove = 0.15

class Color:
    lightBlue = (50, 168, 166)
    darkBlue = (50 ,131, 168)
    green = (0, 255, 128)
    black = (0, 0, 0)
    red = (255, 0, 0)

class MoveDirection:
    right = 0
    left = 1
    up = 2
    down = 3
    none = 4
