from src.Vehicle import Vehicle


class MoonRover(Vehicle):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.angle = 0

    def rotate(self, rotation):
        self.angle += rotation