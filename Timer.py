import time

class Timer:

    def __init__(self, timeToElapse):
        self.lastSavedTime = 0
        self.timeToElapse = timeToElapse
    
    def start(self):
        self.lastSavedTime = time.time()
    
    def timeElapsed(self):
        currentTime = time.time()
        if (currentTime - self.lastSavedTime) > self.timeToElapse:
            self.lastSavedTime = currentTime
            return True
        return False