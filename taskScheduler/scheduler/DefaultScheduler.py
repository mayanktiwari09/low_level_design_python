import heapq
import time
from threading import Condition
from scheduler.SchedulerAlgorithm import SchedulerAlgorithm
from concurrent.futures import ThreadPoolExecutor

maxWorkers = 10

class DefaultScheduler(SchedulerAlgorithm):
    def __init__(self):
        self.actions = list()
        self.cond = Condition()
        self.sleep = 0
        self.executor = ThreadPoolExecutor(max_workers=maxWorkers)

    def addTaskToQueue(self, action):
        # add exec_at time for the action
        action.execute_at = time.time() + action.exec_secs_after

        self.cond.acquire()
        heapq.heappush(self.actions, action)
        self.cond.notify()
        self.cond.release()

    def start(self):
        while True:
            self.cond.acquire()
            while len(self.actions) == 0:
                self.cond.wait()
            # while len(self.actions) != 0:
            #     # calculate sleep duration
            #     next_action = self.actions[0]
            #     sleep_for = next_action.execute_at - time.time()
            #     if sleep_for <= 0:
            #         # time to execute action
            #         break
            #     self.cond.wait(timeout=sleep_for)

            while self.actions and self.actions[0].execute_at - time.time() > 0:
                self.cond.wait(timeout=self.actions[0].execute_at - time.time())

            actionsToExecute = []
            while self.actions and self.actions[0].execute_at - time.time() <= 0:
                actionsToExecute.append(heapq.heappop(self.actions))

            for action in actionsToExecute:
                self.executor.submit(action.execute)
                if action.recurring:
                    self.addTaskToQueue(action)

            self.cond.release()