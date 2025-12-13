from collections import defaultdict

class RouteManager:
    def __init__(self):
        self.flights = defaultdict(set)

    def addRoute(self,start,end):
        self.flights[start].add(end)
        
    def countRoutes(self,start, end): 
        return len(self._findRoutesInner(start, end))
    
    def shortestRoute(self,start,end): 
        pathList = self._findRoutesInner(start, end)
        return min(map(lambda x: len(x),pathList))
    
    def longestRoute(self,start,end):
        pathList = self._findRoutesInner(start, end) 
        return max(map(lambda x: len(x),pathList))

    # findroutesinner records /stores list of paths, which is not directly a requirement, but may be useful , i believ eit could be removed if preferred 
    def _findRoutesInner(self, start, end, route={}, pathList=[]): # records /stores list of paths, which is not directly a requirement, but may be useful , i believ eit could be removed if preferred 
        #numPaths=0
        #print(start)
        #print(f"{route=}")
        for device in self.flights[start]:
            if device in route:
                #print('already visited', f"{device=}")
                continue

            elif device == end:
                route[start]=device
                pathList.append(route)
                #numPaths += 1
                continue
            route[start]=device
            """if device in memo:
                print(memo, start)
                numPaths+=memo[device]
                continue
            """
            self._findRoutesInner(device,end,route.copy(),pathList)
        
        
        return pathList 
    
flights=RouteManager()

flights.addRoute('aaa','bbb')
flights.addRoute('ggg','hhh')
flights.addRoute('aaa','ccc')
flights.addRoute('bbb','ddd')
flights.addRoute('ccc','ddd')
flights.addRoute('aaa','ddd')
flights.addRoute('aaa','ggg')
flights.addRoute('ggg','ccc')
flights.addRoute('ggg','ddd')
print(flights.countRoutes('aaa','ddd'))
print(flights.longestRoute('aaa','ddd'))
print(flights.shortestRoute('aaa','ddd'))