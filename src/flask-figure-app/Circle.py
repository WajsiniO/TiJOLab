from Figure import Figure
from Service import Service
import matplotlib

class Circle(Figure):
    def __init__(self):
        self.type = "square"
        self.color = matplotlib.colors.cnames["grey"]

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type