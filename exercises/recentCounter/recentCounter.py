from collections import defaultdict

class RecentCounter:
    def __init__(self,value:float):
        self.duration = value * 1000
        self.currentstate = defaultdict(list)
    def ping(self,user:str,timeStamp:int):
        self.currentstate[user].append(timeStamp)
        return len([item for item in self.currentstate[user] if item>=timeStamp-self.duration])
    def get_all(self,user:str):
        return self.currentstate[user]
