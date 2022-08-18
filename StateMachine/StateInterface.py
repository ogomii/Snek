import abc


class State:
    initState = 0
    choiceState = 1
    hamiltonState = 2
    playState = 3


class StateInterface(abc.ABC):

    @abc.abstractmethod
    def run(self) -> State:
        pass