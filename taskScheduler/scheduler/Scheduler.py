from scheduler.SchedulerInterface import SchedulerInterface
from scheduler.DefaultScheduler import DefaultScheduler
import threading

class Scheduler(SchedulerInterface):
    # Creatiing a static private variable (private because to not allow access from outside)
    __instance = None  # Syntax to declare a static variable in python (just declare the variable outside __init__())
    __lock = threading.Lock()

    # In python we cannot make the constructor private hence, we need to control its access
    def __init__(self):
        if Scheduler.__instance is None:
            with Scheduler.__lock:
                super().__init__(DefaultScheduler())
                Scheduler.__instance = self      # Syntax to use a static variable in python
        else:
            raise Exception("Singleton instance already exists. Use get_instance() to get the instance.")

    def addAction(self, action):
        self.algorithm.addTaskToQueue(action)

    def startExecution(self):
        self.algorithm.start()

    @staticmethod
    def getInstance():
        if Scheduler.__instance is None:
            with Scheduler.__lock:
                if Scheduler.__instance is None:
                    Scheduler.__instance = Scheduler()
        return Scheduler.__instance