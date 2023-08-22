from abc import ABC, abstractmethod

class Store(ABC):

    @abstractmethod
    def put(self,key,value):
        pass

    @abstractmethod
    def get(self,key):
        pass

    @abstractmethod
    def remove(self,key):
        pass