from ISP.IHumanWorker import IHumanWorker
from ISP.IWorker import IWorker


class HumanWorker(IWorker, IHumanWorker):
    def work(self):
        print("Human worker working")

    def eat(self):
        print("Human worker eating")