from abc import ABC, abstractclassmethod


class IAuto(ABC):

    @abstractclassmethod
    def locomover(self):
        pass

    @abstractclassmethod
    def ligar(self):
        pass