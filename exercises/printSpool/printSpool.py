#!/usr/bin/env python

import argparse
import time
from collections import deque
from functools import wraps
from abc import ABC, abstractmethod
from typing import Union, Callable


def parse_args():
    """
    creating a Command Line Interface to parse arguments.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile", type=str, help = 'input file with commands for printer spooler')
    parser.add_argument("outputFile", type=str, help = 'output file to write output from printer spooler')
    parser.add_argument('-l','--list',action='store_true',help='use list instead of queue')
    return parser.parse_args()

class PrintSpooler(ABC):
    @abstractmethod
    def add_document(self,name:str) -> None:
        pass

    def print_next(self) -> Union[str,None]:
        pass
    
    def peek(self) -> Union[str,None]:
        pass

    def __len__(self) -> int:
        pass


class PrintSpoolerList(PrintSpooler):
    def __init__(self) -> None:
        self.queue: list[str] = []
    
    def add_document(self,name:str) -> None:
        self.queue.append(name)

    def print_next(self) -> Union[str,None]:
        if self.queue==[]:
            return None
        return self.queue.pop(0)
    
    def peek(self) -> Union[str,None]:
        if self.queue==[]:
            return None
        return self.queue[0]

    def __len__(self) -> int:
        return len(self.queue)
    

class PrintSpoolerQueue(PrintSpooler):
    def __init__(self) -> None:
        self.queue: deque = deque()
    
    def add_document(self,name:str) -> None:
        self.queue.append(name)

    def print_next(self) -> Union[str,None]:
        if len(self)==0:
            return None
        return self.queue.popleft()
    
    def peek(self) -> Union[str,None]:
        if len(self)==0:
            return None
        return self.queue[0]

    def __len__(self) -> int:
        return len(self.queue)


def timing(func: Callable[[list[str],PrintSpooler],list[str]]):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start: float = time.perf_counter()
        result: list[str] = func(*args, **kwargs)
        end: float = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timing
def simulate(commands: list[str],printspool: PrintSpooler)-> list[str]:
    output: list = []
    for cmd in commands:
        if cmd == 'PRINT':
            step = printspool.print_next() 
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
        newSpool=PrintSpoolerList()
    else:
        newSpool = PrintSpoolerQueue()
    output = simulate(commands,newSpool)

    with open(args.outputFile, 'w') as f:
        f.writelines(item + '\n' for item in output)



if __name__ == '__main__':
    main()