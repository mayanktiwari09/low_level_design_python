from DAO.DataStore import DataStore
from Model.Store import Store


class HashMapStore(Store):
    def __init__(self,capacity,algorithm):
        self.store = DataStore(capacity,algorithm)

    def put(self, key, value):
        return self.store.put(key,value)

    def get(self, key):
        return self.store.get(key)

    def remove(self, key):
        return self.remove(key)