import time
from functools import wraps
from typing import Tuple, Union, Optional

def timer_attribute(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        wrapper.last_runtime = duration # Store the last runtime
        return result
    wrapper.last_runtime = 0 # Initialize last runtime attribute
    return wrapper


class Autocomplete:
    def __init__(self,filename: str) -> None:
        with open(filename) as f:
            self.words= f.readlines()
            self.words = [line.strip() for line in self.words]
            self.words.sort()
            print(self.words[-1], len(self.words)-1)
        self.prompt()

    def prompt(self):
        prefix=input('Type a prefix: ').lower()
        if prefix and prefix in 'qx':
            if self.quit_program():
                return
        if prefix:
            firstindex, lastindex = self._findFirstAndLastIndices(prefix)
            self.print_results(firstindex,lastindex)
            
        self.prompt()
        
    def print_results(self,firstIdx: int, secondIdx: int) -> None:
        if secondIdx ==-1:
            print('No results found')
            return
        
        additionalResults: int = secondIdx-firstIdx-19
        for i in range(min(20,secondIdx-firstIdx+1)):
            print(self.words[firstIdx+i])
        if additionalResults>0:
            print(f'{additionalResults} more results found')
        print(f'Results found in {self._findFirstAndLastIndices.last_runtime*1000:.5f} milliseconds')    



    def quit_program(self) -> bool:
        escape = input('Are you trying to exit the program? (y/n): ').lower()
        if escape == 'y':
            return True
        elif escape == 'n':
            return False
        else:
            print('Answer with y or n')
            return self.quit_program()
        
    @timer_attribute
    def _findFirstAndLastIndices(self, prefix: str) -> Tuple[int,int]: 
        firstindex=self._binarySearchBoth(prefix)
        lastindex = -1
    
        if firstindex!=-1:
            lastindex=self._binarySearchBoth(prefix,start=firstindex,last=True)
        return firstindex, lastindex 
    
    
    def _binarySearchBoth(self, prefix: str, start: int = 0, last: bool = False) -> int:
        length=len(prefix)
        left=start
        right=len(self.words)-1 
        idx=-1
        
        while left<=right and idx<0:
            pointer=left + (right-left)//2
            comparePrefix=self.words[pointer][:length]
            compareNext = self.words[(pointer+1)%len(self.words)][:length]
            comparePrev = self.words[pointer-1][:length]
            #print(f'{prefix=},{pointer=},{comparePrev=},{comparePrefix=},{compareNext=}')
            if comparePrefix==prefix:
                if last:
                    if pointer == len(self.words)-1 or compareNext>prefix:
                        idx=pointer
                        #print(f'{prefix=},{last=},{idx=}')
                    left = pointer+1
                else:
                    if pointer == 0 or comparePrev<prefix:
                        idx=pointer
                        #print(f'{prefix=},{last=},{idx=}')
                    right = pointer-1

            elif comparePrefix > prefix:
                right = pointer - 1
            
            elif comparePrefix < prefix:
                left = pointer + 1

        #print(f'done, {idx=}')
        return idx


a=Autocomplete('words_alpha.txt')