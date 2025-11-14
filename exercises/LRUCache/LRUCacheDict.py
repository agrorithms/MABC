from collections import OrderedDict
from typing import Iterator,Any

_sentinel = object()
class LRUCacheDict:
    def __init__(self,capacity: int) -> None:
        '''
        space complexity O(n) up to n == capacity, where n is number of keys stored. if over capacity, oldest item is removed
        ordered dict consists of hash table and a doubly linked list
        '''
        self.cache: OrderedDict = OrderedDict()
        self.capacity: int = capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        '''
        setitem is O(1) time complexity in that it does not depend on the current size of the cache. 
        if reorder is needed, .move_to_end accesses the node via a hash table for O(1) lookup - doesnt need to loop through the linked list. 
        then unlinking and relinking in the linked list is also O(1)

        popping is O(1) - access LRU item at end of LL and remove
        setting is O(1) - hash table
        '''
        
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache)>=self.capacity:
            self.cache.popitem(last=False)
           
        self.cache[key]=value
        
            
    def __getitem__(self,key: Any) -> Any:
        '''
        O(1) same as setitem but we never need to pop nor set
        '''
        if key not in self.cache:
            raise KeyError(f"Key '{key}' not found in LRU Cache.")
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def __contains__(self,key: Any) -> bool:
        '''
        O(1) lookup via hashtable
        '''
        return key in self.cache
    
    def __len__(self) -> int:
        '''
        O(1) len() is already stored
        '''
        return len(self.cache)

    def __iter__(self) -> Iterator[Any]:
        '''
        O(1) - creates a view object that references existing data structure - no traversal , no copying, nothing is created.
        Even with reverse , it doesn't actually reverse up front
        '''
        return reversed(self.cache.keys())
    
    def get(self,key:Any, default: Any = None) -> Any:
        '''
        O(1) - same as __getitem__ in terms of big O time complexity
        '''

        if key not in self.cache:
            return default
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    
    def pop(self,key:Any,default: Any =_sentinel) -> Any: # how to type hint the return type with keyerror
        '''
        O(1) - same idea where hashtable provides O(1) lookup

        '''
        if key not in self.cache and default==_sentinel:
            raise KeyError(f"Key '{key}' not found in LRU Cache.")
        else:
            return self.cache.pop(key,default)
            
            
    def __repr__(self) -> str:
        '''
        O(n) need to access each item in the ordereddict so depends on size of ordereddict. again n <=self.capacity so this caps out.
        '''
        output = '{'
        for key in self:
            output+=f'{key} : {self.cache[key]}, '
        return output[:-2] + '}'