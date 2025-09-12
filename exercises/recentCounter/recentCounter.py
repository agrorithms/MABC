from collections import defaultdict

class RecentCounter:
    def __init__(self,value:float):
        self.duration = value * 1000
        self.currentstate = defaultdict(list)
    '''
    def ping(self,user:str,timeStamp:int):
        pinglist=self.currentstate[user]
        pinglist.append(timeStamp)
        count=0
        for i in reversed(range(len(pinglist))):
            if(pinglist[i]>=timeStamp-self.duration):
                count+=1
            else:
                break
        return count
        
        #return len([item for item in self.currentstate[user] if item>=timeStamp-self.duration])
    '''
    def get_all(self,user:str):
        return self.currentstate[user]

    def ping(self,user:str, timeStamp:int):
        pinglist=self.currentstate[user]
        pinglist.append(timeStamp)
        
        cutoff=timeStamp-self.duration
        pointer = len(pinglist)//2 
        step=pointer//2 
        prevstep=step
        if pinglist[0]>=cutoff:
            return len(pinglist)

        
        
        while prevstep>0:
            if pinglist[pointer]>=cutoff: 
                if pinglist[pointer-1]<cutoff:
                    return len(pinglist)-pointer
                pointer-=step 
                
            else:
                if pinglist[pointer+1]>=cutoff:
                    return len(pinglist)-pointer-1
                pointer+=step
    
            prevstep=step
            step//=2  


