# Usage
from ISP.HumanWorker import HumanWorker
from ISP.RobotWorker import RobotWorker

human = HumanWorker()
robot = RobotWorker()

human.eat()  # Works!
robot.eat()  # Exception!