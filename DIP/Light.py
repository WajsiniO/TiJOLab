class Light:
    def __init__(self):
        self.default_state = False
        self.state = self.default_state

    def press(self):
        if not self.state:
            self.state = True
            print("Light is spinning")
        else:
            self.state = False
            print("Light is stopped")

