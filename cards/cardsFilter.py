#!/usr/bin/env python3

import csv
import heapq
import argparse


def parse_args():
    """
    creating a Command Line Interface to parse arguments.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("minOnBase", type=int)
    parser.add_argument("outcome", type=str)
    parser.add_argument("position", type=str)
    parser.add_argument("minFielding", type=int)


    parser.add_argument("--write", "-w", action="store_true", help="write output to csv")

    return parser.parse_args()

def fieldingFilter(player: dict, desiredPos:str, minFieldStat:int):
    """returns True if a single player meets fielding critera
    by qualifying for a position and having at least a minimum fielding stat at that position"""

    positionIdx=player['Position'].find(desiredPos)

    #first look for "general" positions like OF/ IF which qualify for any infield / outfield position
    if positionIdx==-1:
        if desiredPos in ('1B','2B','3B','SS'):

            positionIdx=player['Position'].find('IF')

        elif desiredPos in ('LF','CF','RF'):
            positionIdx=player['Position'].find('OF')

    #if desired position or general quaifying position is present, look for the the fielding value by ffinding the next '+' after given position
    if positionIdx!=-1:
        commaIdx=player['Position'].find(',',positionIdx)
        if commaIdx==-1:

            fielding = int(player['Position'][player['Position'].find('+',positionIdx)+1:])
        else:

            fielding = int(player['Position'][player['Position'].find('+',positionIdx)+1:commaIdx])
        return fielding >=minFieldStat
    # qualify any position for 1B and set filelding to -1 or -2 based on position
    elif desiredPos=='1B':
        if player['Position']=='---' or player['Position']=='--':
            return -2>=minFieldStat
        else:
            return -1>=minFieldStat
    return False





def cardsFilter(minOnBase: int, outcome: str,position: str, minFielding: int):

    with open('cardsDataPositionPlayers.csv', 'r', newline='') as f:
        reader=csv.DictReader(f)
        playerList=list(reader)
        hitMap={'S':'Single','DB':'Double',"TR":'Triple',"HR":'Home Run'}
        hitList=[]
        threeLow=[]

        # loop through players skipping headers and skipping players below minimnum on base requirement
        for i,player in enumerate(playerList):

            if int(player['OnBase'])<minOnBase:                                         #skip over players below minOnBase
                continue

            if not fieldingFilter(player, position, minFielding):                       #skip over players who do not qualify at position
                continue                                                                #or do not meet minFielding criteria at given position


        #best way i could think of to stop at either a '+' or '-'
            for j in range(len(player[hitMap[outcome]])):
                if player[hitMap[outcome]][j]=='-' or player[hitMap[outcome]][j]=='+':
                    lowVal=player[hitMap[outcome]][0:j]
                    break

            if lowVal == '':
                continue
        #use a heap to keep the lowest 3 values
            if len(hitList)<3:
                heapq.heappush(hitList,(-int(lowVal),i))
            else:
                heapq.heappushpop(hitList,(-int(lowVal),i))


        #this seems clunky but to resort these guys ascending i make a list and loop it backwards
        for i in range(len(hitList)):
            threeLow.append(heapq.heappop(hitList)[1])


        for i in range(len(threeLow)):
            hitList.append(playerList[threeLow[-i-1]])


            #need to return the dictionaries or write to csv instead of printing
        return hitList


def main():
    args=parse_args()

    output = cardsFilter(args.minOnBase, args.outcome, args.position, args.minFielding)

    print(output)

    if args.write:
        headers = output[0].keys()

        with open('output.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(output)

if __name__ == '__main__':
    main()
