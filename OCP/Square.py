from Figure import Figure

class Square(Figure):
    def __init__(self, a):
        self.a = a

    def draw(self):
        for _ in range(self.a):
            print(self.a * "o ")
        print()









