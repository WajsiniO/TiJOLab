from Square import Square
from Triangle import Triangle
from FigureDrawer import FigureDrawer

class FigureInitializer:
    def __init__(self, a, h):
        self.a = a
        self.h = h
        self.square = Square(a)
        self.triangle = Triangle(h)

    def draw_figures(self):
        drawer = FigureDrawer()
        drawer.draw(self.square)
        drawer.draw(self.triangle)


figure_initializer = FigureInitializer(5, 5)
figure_initializer.draw_figures()