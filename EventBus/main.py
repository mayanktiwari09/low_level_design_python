import time

from EventBus import EventBus
from Model.Event import Event, EventType

bus = EventBus(10,10)
bus.addTopics('log')
bus.addPublishers('Mayank','log')
bus.addSubscribers('Kunal','log')

e = Event('Mayank',EventType.ERROR, 'testLog', time.time())
bus.put(e, 'Mayank', 'log')
result = bus.pull('Kunal','log').result()
print(result.get_id())
