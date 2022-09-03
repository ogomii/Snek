import abc


class State:
    initState = 0
    choiceState = 1
    hamiltonState = 2
    playState = 3
    shutDown = 4
    gameOver = 5


class StateInterface(abc.ABC):

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def isState(self, currentState) -> bool:
        pass