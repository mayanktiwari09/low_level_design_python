from concurrent.futures.thread import ThreadPoolExecutor
import queue

class Executor:
    def __init__(self,publisherThreads, subscriberThreads):
        self.PublisherExecutors = [ThreadPoolExecutor(max_workers=1) for _ in range(publisherThreads)]
        self.SubscriberExecutors = [ThreadPoolExecutor(max_workers=1) for _ in range(subscriberThreads)]

    def put(self, event, q: queue, key):
        return self.PublisherExecutors[hash(key) % len(self.PublisherExecutors)].submit(q.put, event)

    def pull(self, q: queue, key):
        return self.SubscriberExecutors[hash(key) % len(self.SubscriberExecutors)].submit(q.get)



