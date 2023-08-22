from Cache import Cache
from Model.EvictionStrategy import EvictionStrategy

cache = Cache(10,EvictionStrategy.LRU)
cache.put('hello','world')
print(cache.get('hello'))