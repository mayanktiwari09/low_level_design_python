from enum import Enum

class EvictionStrategy(Enum):
    LRU = 1
    LFU = 2
    MRU = 3