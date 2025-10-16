#!/usr/bin/env python

import argparse
import time
from collections import deque
from functools import wraps

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

def parse_args():
    """
    creating a Command Line Interface to parse arguments.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile", type=str, help = 'input file with commands for printer spooler')
    parser.add_argument("outputFile", type=str, help = 'output file to write output from printer spooler')
    parser.add_argument('-l','--list',action='store_true',help='use list instead of queue')
    return parser.parse_args()


class PrintSpoolerList:
    def __init__(self):
        self.queue=[]
    
    def add_document(self,name:str):
        self.queue.append(name)

    def print_next(self):
        if self.queue==[]:
            return None
        return self.queue.pop(0)
    
    def peek(self):
        if self.queue==[]:
            return None
        return self.queue[0]

    def __len__(self):
        return len(self.queue)
    

class PrintSpoolerQueue:
    def __init__(self):
        self.queue=deque()
    
    def add_document(self,name:str):
        self.queue.append(name)

    def print_next(self):
        if len(self)==0:
            return None
        return self.queue.popleft()
    
    def peek(self):
        if len(self)==0:
            return None
        return self.queue[0]

    def __len__(self):
        return len(self.queue)

@timing
def simulate(commands: list[str],queue=True)-> list[str]:
    if queue:
        printspool=PrintSpoolerQueue()
    else:
        printspool = PrintSpoolerList()
    output = []
    for cmd in commands:
        if cmd == 'PRINT':
            step=printspool.print_next()
            if step == None:
                step = 'No documents waiting'
            else:
                step = 'Printing ' + step
            output.append(step)
            print(step)
            

        elif cmd == 'NEXT':
            step=printspool.peek()
            if step == None:
                step = 'Queue empty'
            else: 
                step = 'Next is ' + step
            output.append(step)
            print(step)
        elif cmd[:4]=='SEND':
            printspool.add_document(cmd[5:])
        else:
            return ['Invalid command: ' + cmd]
    return output

def main():
    args=parse_args()
    with open(args.inputFile) as f:
        commands=f.readlines()
        commands = [cmd.strip() for cmd in commands]

    if args.list:
        output=simulate(commands,False)
    else:
        output = simulate(commands)

    with open(args.outputFile, 'w') as f:
        f.writelines(item + '\n' for item in output)



if __name__ == '__main__':
    main()