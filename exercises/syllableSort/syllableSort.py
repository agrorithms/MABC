#!/usr/bin/env python3

import argparse

def parse_args():
    """
    creating a Command Line Interface to parse arguments. user should pass 1 argument, within that argument, items are separated by commas
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("wordList", type=str, help = 'comma separated list')

    return parser.parse_args()


def countSyllables(word:str):
    """

    """

    syllableCount=0
    for i in range(len(word)):
        if i==0:
            if word[i] in 'aeiouyAEIOUY':
                syllableCount+=1
                vowel=True
            else:
                vowel=False
        elif word[i] in 'aeiouyAEIOUY':
            if vowel:
                continue
            else:
                syllableCount+=1
                vowel=True
        else:
            vowel=False

    return syllableCount

def syllableSort(wordList:list[str]):

    wordList.sort(key= lambda x: (countSyllables(x),x))
    return wordList

def main():
    args=parse_args()
    output = syllableSort(args.wordList.split(','))
    print(output)


if __name__ == '__main__':
    main()
