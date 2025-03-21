from Figure import Figure

class Triangle(Figure):
    def __init__(self, h):
        self.h = h

    def draw(self):
        for side in range(1, self.h + 1):
            print(side * "o ")
        print()