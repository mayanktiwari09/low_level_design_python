from DAO.DataStoreInterface import DataStoreInterface
from DAO.LRU import LRU


class DataStore(DataStoreInterface):
    def __init__(self, capacity, algorithm):
        if algorithm.value == 1:
            self.map = {}
            super().__init__(LRU(capacity,self.map))

    def get(self,key):
        return self.storeManager.get(key)

    def put(self,key,value):
        return self.storeManager.put(key,value)

    def remove(self,key):
        return self.storeManager.remove(key)