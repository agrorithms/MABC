#!/usr/bin/env python3

import argparse

def parse_args():
    """
    creating a Command Line Interface to parse arguments. user should pass 1 argument, within that argument, items are separated by commas
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("nameList", type=str, help = 'comma separated list')

    return parser.parse_args()


def customNameSort(nameList:list[str]):
    """
    sorts a list of strings by length, then reverse alphabetical (case insensitive). with a special case,
    if both 'bros' and 'hoes' exist in the list, then sorting will place 'bros' at the index preceding 'hoes'
    """
    sortcriteria={}

    #loop through strings in list. convert to lower for case insensitive. add every lowercase word to a dictionary
    #this maps each word to a list that will be used to sort by length,then reverse alphabetical
    for word in nameList:
        wordLower=word.lower()
        if wordLower not in sortcriteria:
            sortcriteria[wordLower]=[len(wordLower)]
            for char in wordLower:
                sortcriteria[wordLower].append(-ord(char))

    #if both bros and hoes exist, give bros alphabetical sorting equal to hoes, and append a tiebreaker item - 0 for bros , 1 for hoes
    if 'bros' in sortcriteria and 'hoes' in sortcriteria:
        sortcriteria['bros']=sortcriteria['hoes'][:]
        sortcriteria['bros'].append(0)
        sortcriteria['hoes'].append(1)
    nameList.sort(key=lambda x: sortcriteria[x.lower()])
    return nameList


def main():
    args=parse_args()
    output = customNameSort(args.nameList.split(','))
    print(output)


if __name__ == '__main__':
    main()
