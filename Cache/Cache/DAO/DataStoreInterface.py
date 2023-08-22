from abc import ABC, abstractmethod
from DAO.EvictionPolicy import EvictionPolicy


class DataStoreInterface(ABC):
    def __init__(self, algorithm: EvictionPolicy):
        self.storeManager = algorithm

    @abstractmethod
    def get(self,key):
        pass

    @abstractmethod
    def put(self,key,value):
        pass

    @abstractmethod
    def remove(self,key):
        pass