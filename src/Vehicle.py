from abc import abstractmethod

class Vehicle:
    @abstractmethod
    def driveForward(self, distance):
        pass

    @abstractmethod
    def driveBackward(self, distance):
        pass

    @abstractmethod
    def turnRight(self, rotation):
        pass

    @abstractmethod
    def turnLeft(self, rotation):
        pass

    @abstractmethod
    def rotate(self, rotation):
        pass

    @abstractmethod
    def startPoint(self):
        pass

    @abstractmethod
    def localPoint(self):
        pass


