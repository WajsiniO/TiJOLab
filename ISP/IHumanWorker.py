from abc import ABC, abstractmethod


class IHumanWorker(ABC):
    @abstractmethod
    def eat(self):
        pass