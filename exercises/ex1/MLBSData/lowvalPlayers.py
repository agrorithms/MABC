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


    return parser.parse_args()

def findLowValPlayer(minOnBase: int, outcome: str):
    with open('MLB Showdown Raw Data Position Players.csv', 'r') as f:
        reader = csv.reader(f)
        playerStats = list(reader)
        hitmap={'S':16,'DB':18,"TR":19,"HR":20}
        hitList=[]
        selectedHit=hitmap[outcome]
        threeLow=[]

        # loop through players skipping headers and skipping players below minimnum on base requirement
        for i, player in enumerate(playerStats[1:]):
            if int(player[6])<minOnBase:
                continue

        #best way i could think of to stop at either a '+' or '-'
            for j in range(len(player[selectedHit])):
                if player[selectedHit][j]=='-' or player[selectedHit][j]=='+':
                    lowVal=player[selectedHit][0:j]
                    break

            if lowVal == '':
                continue
        #use a heap to keep the lowest 3 values
            if len(hitList)<3:
                heapq.heappush(hitList,(-int(lowVal),i+1))
            else:
                heapq.heappushpop(hitList,(-int(lowVal),i+1))
            #if len(hitList)>3:
            #    heapq.heappop(hitList)

        #this seems clunky but to resort these guys ascending i make a list and loop it backwards
        for i in range(len(hitList)):
            threeLow.append(heapq.heappop(hitList))
        for i in range(len(threeLow)):
            print(playerStats[threeLow[-i-1][1]])

def main():
    args=parse_args()

    findLowValPlayer(args.minOnBase, args.outcome)

if __name__ == '__main__':
    main()
