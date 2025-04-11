from abc import ABC, abstractmethod

class Figure:
    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def set_new_color(self, color):
        pass

    @abstractmethod
    def get_type(self):
        pass