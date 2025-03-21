from DIP.Button import Button

class Fan(Button):
    def __init__(self):
        self.default_state = False
        self.state = self.default_state

    def press(self):
        if not self.state:
            self.state = True
            print("Fan is spinning")
        else:
            self.state = False
            print("Fan is stopped")


