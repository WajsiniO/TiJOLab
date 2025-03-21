from DIP.Light import Light
from abc import ABC, abstractmethod


class Button:
    @abstractmethod
    def press(self):
        pass