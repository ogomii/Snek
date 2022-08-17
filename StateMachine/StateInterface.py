import abc


class State:
    choiceState = 1
    playState = 2


class StateInterface(abc.ABC):

    @abc.abstractmethod
    def run(self) -> State:
        pass