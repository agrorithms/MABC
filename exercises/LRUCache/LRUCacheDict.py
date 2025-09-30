class LRUCacheDict:
    def __init__(self,capacity):
        self.cache={}
        self.capacity=capacity
        self.recency=[]
        self.size=0

    def __setitem__(self, key, value):
        
        if key in self.recency:
            self.recency.pop(self.recency.index(key))
            self.size-=1
        elif key not in self.cache and self.size>=self.capacity:
            evict=self.recency.pop(0)
            del self.cache[evict]
            self.size-=1
        
        self.cache[key]=value
        self.size+=1
        self.recency.append(key)
            
    def __getitem__(self,key):
        if key not in self.cache:
            raise KeyError(f"Key '{key}' not found in LRU Cache.")
        else:
            self.recency.append(self.recency.pop(self.recency.index(key)))
            return self.cache[key]

    def __contains__(self,key):
        return key in self.cache
    
    def __len__(self):
        return self.size

    def __iter__(self):
        return self.cache.keys()
    
    def get(self,key, default = None):
        if key not in self.cache:
            return default
        else:
            self.recency.append(self.recency.pop(self.recency.index(key)))
            return self.cache[key]
    
    def pop(self,key,default=None):
        if key not in self.cache:
            if default==None:
                raise KeyError(f"Key '{key}' not found in LRU Cache.")
            else:
                return default
        else:
            self.recency.pop(self.recency.index(key))
            evict=self.cache[key].pop()
            self.size-=1
            return evict
            
    def __repr__(self):
        output = '{'
        for key in self.cache.keys():
            output+=f'{key} : {self.cache[key]}, '
        return output[:-2] + '}'