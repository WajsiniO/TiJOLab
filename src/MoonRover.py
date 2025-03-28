from src.Vehicle import Vehicle


class MoonRover(Vehicle):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.angle = 0

    def rotate(self, rotation):
        if rotation is None:
            return None
        self.angle += rotation

    def reset(self):
        self.angle = 0

    def driveForward(self, distance):
        if distance is None:
            return None

        if self.angle == -360:
            self.reset()

        if self.angle == 0:
            self.Y += distance
        elif self.angle == 180 or self.angle == -180:
            self.Y -= distance
        elif self.angle == 90 or self.angle == -270:
            self.X += distance
        elif self.angle == 270 or self.angle == -90:
            self.X -= distance

    def driveBackward(self, distance):

        if distance is None:
            return None

        if self.angle == -360:
            self.reset()

        if self.angle == 0:
            self.Y -= distance
        elif self.angle == 180 or self.angle == -180:
            self.Y += distance
        elif self.angle == 90 or self.angle == -270:
            self.X -= distance
        elif self.angle == 270 or self.angle == -90:
            self.X += distance

    def localPoint(self):
        if self.angle == 0:
            zwrot = "North"
        elif self.angle == 90 or self.angle == -270:
            zwrot = "East"
        elif self.angle == 180 or self.angle == -180:
            zwrot = "South"
        elif self.angle == 270 or self.angle == -90:
            zwrot = "West"
        else :
            zwrot = "None"
        print(self.Y, self.X, zwrot)




def main():
    krzys = MoonRover(0, 0)
    krzys.driveForward(10)
    krzys.localPoint()
    krzys.rotate(90)
    krzys.driveBackward(30)
    krzys.localPoint()

if __name__ == "__main__":
    main()