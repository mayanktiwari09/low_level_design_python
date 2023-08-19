from abc import ABC, abstractmethod
from scheduler.SchedulerAlgorithm import SchedulerAlgorithm

class SchedulerInterface(ABC):

    def __init__(self,SchedulerAlgorithm: SchedulerAlgorithm):
        self.algorithm = SchedulerAlgorithm

    @abstractmethod
    def addAction(self, action):
        pass

    @abstractmethod
    def startExecution(self):
        pass
