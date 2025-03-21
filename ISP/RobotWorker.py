from ISP.IWorker import IWorker


class RobotWorker(IWorker):
    def work(self):
        print("Robot worker working")

    def eat(self):
        raise NotImplementedError("Robots don't eat")