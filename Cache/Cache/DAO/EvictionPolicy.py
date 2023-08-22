from abc import ABC, abstractmethod

class EvictionPolicy(ABC):

    @abstractmethod
    def get(self,key):
        pass

    @abstractmethod
    def put(self,key,value):
        pass

    @abstractmethod
    def remove(self,key):
        pass
