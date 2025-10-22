
class TimeRange:
    def __init__(self,val1:float,val2:float):
        self.open=val1
        self.close=val2
    def __lt__(self,other):
        return self.open<other.open
    def __eq__(self,other):
        if not isinstance(other,TimeRange):
            return False
        return self.close==other.close and self.open==other.open
    def __len__(self):
        if self.close>=self.open:
            return self.close - self.open
        else:
            return 24-self.open + self.close
    def __repr__(self):
        return f'TimeRange(open = {self.open}, close = {self.close})'
    def isWrapped(self):
        return self.close<self.open
    
    

def isInRange(openHours:TimeRange,targetHours:TimeRange):
        '''
        assume open is always less than close based on isWrapped handling in the isCovered method, 
        which is the only place this function is called
        '''
        return targetHours.open>=openHours.open and targetHours.close<=openHours.close

class BankHours:
    def __init__(self,bankHoursList:list[TimeRange]):
        self.updateBankHours(bankHoursList)
    
    def updateBankHours(self,newBankHours:list[TimeRange]):
        for i,bank in enumerate(newBankHours):
            if bank.isWrapped():
                newBankHours.append(TimeRange(0,bank.close))
                newBankHours[i].close=24
        newBankHours.sort()
        openHours=[newBankHours[0]]
        pointer=0
        for bankRange in newBankHours[1:]:

            if bankRange.open<=openHours[pointer].close:
                openHours[pointer].close=max(bankRange.close,openHours[pointer].close)
            else:
                openHours.append(bankRange)
                pointer+=1
        self.hours=openHours
    

    def isCovered(self,tradeHours:TimeRange):
        if tradeHours.isWrapped():
            return self.isCovered(TimeRange(0,tradeHours.close)) and self.isCovered(TimeRange(tradeHours.open,24))            
             
        return any(isInRange(openHours,tradeHours) for openHours in self.hours)
                   
    
    def __repr__(self):
        out='BankHours('
        for hours in self.hours:
            out+= f'({hours.open},{hours.close})'
        return out+')'
    