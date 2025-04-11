from Figure import Figure
import matplotlib

class Square(Figure):
    def __init__(self):
        self.type = "square"
        self.color = matplotlib.colors.cnames["grey"]

    def set_new_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type








