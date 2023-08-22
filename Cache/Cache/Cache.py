import threading

from Model.EvictionStrategy import EvictionStrategy
from Model.HashMapStore import HashMapStore


class Cache():
    __instance = None  # Syntax to declare a static variable in python (just declare the variable outside __init__())
    __lock = threading.Lock()

    def __init__(self, size, evictionStrategy: EvictionStrategy):
        if Cache.__instance is None:
            with Cache.__lock:
                self.store = HashMapStore(size,evictionStrategy.LRU)
                Cache.__instance = self
        else:
            raise Exception("Singleton instance already exists. Use get_instance() to get the instance.")

    @staticmethod
    def getInstance():
        if Cache.__instance is None:
            with Cache.__lock:
                if Cache.__instance is None:
                    Cache.__instance = Cache()
        return Cache.__instance

    def get(self,key):
        return self.store.get(key)

    def put(self,key,value):
        return self.store.put(key,value)

    def remove(self,key):
        return self.store.remove(key)
