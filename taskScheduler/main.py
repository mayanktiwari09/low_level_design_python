import time
from threading import Thread

from scheduler.Scheduler import Scheduler
from tasks.DeferredAction import DeferredAction

action1 = DeferredAction(1, ("A",), recurring=True)
action2 = DeferredAction(2, ("B",))
action3 = DeferredAction(3, ("C",))
action4 = DeferredAction(4, ("D",))

executor = Scheduler().getInstance()

t = Thread(target=executor.startExecution, daemon=True)
t.start()

executor.addAction(action1)
executor.addAction(action2)
executor.addAction(action3)
executor.addAction(action4)

# wait for all actions to execute
time.sleep(15)
