from abc import ABC, abstractmethod

class DeferredActionInterface(ABC):
    def __init__(self, exec_secs_after, name):
        self.exec_secs_after = exec_secs_after
        self.name = name
        self.execute_at = None

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def execute(self):
        pass