from collections import OrderedDict

_sentinel = object()
class LRUCacheDict:
    def __init__(self,capacity: int) -> None:
        self.cache: OrderedDict = OrderedDict()
        self.capacity: int = capacity

    def __setitem__(self, key, value) -> None:
        
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache)>=self.capacity:
            self.cache.popitem(last=False)
           
        self.cache[key]=value
        
            
    def __getitem__(self,key):
        if key not in self.cache:
            raise KeyError(f"Key '{key}' not found in LRU Cache.")
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def __contains__(self,key) -> bool:
        return key in self.cache
    
    def __len__(self) -> int:
        return len(self.cache)

    def __iter__(self):
        return reversed(self.cache.keys())
    
    def get(self,key, default = None):
        if key not in self.cache:
            return default
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    
    def pop(self,key,default=_sentinel):
        if key not in self.cache and default==_sentinel:
            raise KeyError(f"Key '{key}' not found in LRU Cache.")
        else:
            return self.cache.pop(key,default)
            
            
    def __repr__(self) -> str:
        output = '{'
        for key in self:
            output+=f'{key} : {self.cache[key]}, '
        return output[:-2] + '}'