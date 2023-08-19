from abc import abstractmethod, ABC


class SchedulerAlgorithm(ABC):

    @abstractmethod
    def addTaskToQueue(self,action):
        pass

    @abstractmethod
    def start(self):
        pass