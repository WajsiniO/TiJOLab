
class Service:
    def __init__(self, figures):
        self.figures = {figure.get_type(): figure for figure in figures}

    def get_colors(self):
        return {ftype: figure.get_color() for ftype, figure in self.figures.items()}

    def set_color(self, figure_type, new_color):
        if figure_type in self.figures:
            self.figures[figure_type].set_new_color(new_color)
            return True
        return False

    def set_color_all(self, new_color):
        for figure in self.figures.values():
            figure.set_new_color(new_color)