
def isInRange(openHours,targetHours):
        return targetHours[0]>=openHours[0] and targetHours[1]<=openHours[1]

class BankHours:
    def __init__(self,bankHoursList):
        self.updateBankHours(bankHoursList)
    
    def updateBankHours(self,newBankHours):
        for i,bank in enumerate(newBankHours):
            if bank[1]<bank[0]:
                newBankHours.append([0,bank[1]])
                newBankHours[i][1]=24
        newBankHours.sort()
        openHours=[newBankHours[0]]
        pointer=0
        for bank in newBankHours[1:]:

            if bank[0]<=openHours[pointer][1]:
                openHours[pointer][1]=max(bank[1],openHours[pointer][1])
            else:
                openHours.append(bank)
                pointer+=1
        self.hours=openHours
    

    def isCovered(self,tradeHours):
        tradeHoursWrap=None
        if tradeHours[1]<tradeHours[0]:
            tradeHoursWrap=[0,tradeHours[1]]
            tradeHours=[tradeHours[0],24]
            wrapHoursPass=False
            print(tradeHours,tradeHoursWrap)
        for openHours in self.hours:
            if isInRange(openHours,tradeHours):
                if tradeHoursWrap==None or wrapHoursPass:
                    return True
            elif tradeHoursWrap and isInRange(openHours,tradeHoursWrap):
                wrapHoursPass = True
        return False        
