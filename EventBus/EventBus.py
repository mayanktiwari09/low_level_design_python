import queue
from Model.Event import Event
from utils.Executor import Executor


class EventBus:
    def __init__(self, publisherThreads, subscriberThreads):
        self.topics = {}
        self.subscribers = {}
        self.publishers = {}
        self.executor = Executor(publisherThreads, subscriberThreads)

    def addTopics(self,topic):
        self.topics[topic] = queue.Queue()

    def addSubscribers(self,subscriber,topic):
        if subscriber in self.subscribers:
            self.subscribers[topic].append(subscriber)
        else:
            self.subscribers[topic] = [subscriber]

    def addPublishers(self,publisher,topic):
        if publisher in self.publishers:
            self.publishers[topic].append(publisher)
        else:
            self.publishers[topic] = [publisher]

    def put(self, event: Event, publisher, topic):
        return self.executor.put(event, self.topics[topic], topic + publisher)

    def pull(self, subscriber, topic):
        return self.executor.pull(self.topics[topic], topic + subscriber)