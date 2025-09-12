from collections import namedtuple

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
    

def isInRange(openHours:TimeRange,targetHours:TimeRange):
        '''
        assume open is always less than close based on tradeHoursWrap handling in the isCovered method, 
        which is the only place this function is called
        '''
        return targetHours.open>=openHours.open and targetHours.close<=openHours.close

class BankHours:
    def __init__(self,bankHoursList:list[TimeRange]):
        self.updateBankHours(bankHoursList)
    
    def updateBankHours(self,newBankHours:list[TimeRange]):
        for i,bank in enumerate(newBankHours):
            if bank.close<bank.open:
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
        tradeHoursWrap=None
        if tradeHours.close<tradeHours.open:
            tradeHoursWrap=TimeRange(0,tradeHours.close)
            tradeHours=TimeRange(tradeHours.open,24)
            wrapHoursPass=False
            #print(tradeHours,tradeHoursWrap)
        for openHours in self.hours:
            if isInRange(openHours,tradeHours):
                if tradeHoursWrap==None or wrapHoursPass:
                    return True
            elif tradeHoursWrap and isInRange(openHours,tradeHoursWrap):
                wrapHoursPass = True
        return False        
