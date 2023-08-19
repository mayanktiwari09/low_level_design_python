import math
import time
from tasks.DeferredActionInterface import DeferredActionInterface

class DeferredAction(DeferredActionInterface):
    def __init__(self, exec_secs_after, name, recurring=False):
        super().__init__(exec_secs_after, name)
        self.recurring = recurring

    def __lt__(self, other):
        return self.execute_at < other.execute_at

    def execute(self):
        print("hi, I am {0} executed at {1} and required at {2}".format(
            self.name, math.floor(time.time()), math.floor(self.execute_at))
        )


