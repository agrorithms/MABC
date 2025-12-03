import time
from functools import wraps
from typing import Tuple, Union

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
        self.prompt()

    def prompt(self):
        prefix=input('Type a prefix: ').lower()
        if prefix in 'qx':
            if self.quit_program():
                return
        if prefix !='':
            firstindex, lastindex = self._findFirstAndLastIndices(prefix)
            self.print_results(firstindex,lastindex)
            
        self.prompt()
        
    def print_results(self,firstIdx: int,secondIdx: int) -> None:
        if firstIdx is None:
            print('No results found')
            return
        
        additionalResults: int = secondIdx-firstIdx-20
        for i in range(min(20,secondIdx-firstIdx)):
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
    def _findFirstAndLastIndices(self, prefix: str) -> Union[Tuple[None,None], Tuple[int,int]]: 
        firstindex=self._binarySearchFirst(prefix)
        lastindex = None
    
        if firstindex!=None:
            lastindex=self._binarySearchLast(prefix,start=firstindex)
        return firstindex, lastindex 
    
    def _binarySearchFirst(self, prefix: str, start: int = 0) -> int:
        length=len(prefix)
        left=start
        right=len(self.words)-1 
        idx=None
        
        while left<=right and not idx:
            pointer=left + (right-left)//2
            if self.words[pointer][:length]>=prefix: 
                if(self.words[pointer-1][:length]<prefix or (pointer == 0 and self.words[pointer][:length]==prefix)):
                    idx=pointer
                right=pointer-1 
                
            else:
                if (pointer == len(self.words)-1):
                    if self.words[pointer][:length]==prefix: 
                        idx=pointer+1
                elif self.words[pointer+1][:length]>=prefix:
                    idx=pointer+1
                
                left=pointer+1
        
        #binary search will find an index where self.words 'crosses' the prefix even if prefix is not found
        #this only returns index if it matches prefix
        if idx!=None and self.words[idx][:length] == prefix:
            #print(f'bsF, idx: {idx}, points to {self.words[idx]}')
            return idx
    
    def _binarySearchLast(self, prefix: str, start: int = 0) -> int:
        length=len(prefix)
        left=start
        right=len(self.words)-1
        idx=None

        while left<=right and not idx:
            pointer=left + (right-left)//2
        
            if self.words[pointer][:length]<=prefix: 
                if((pointer == len(self.words)-1 and self.words[pointer][:length]==prefix) or self.words[pointer+1][:length]>prefix ):
                    idx=pointer+1
                left=pointer+1 
                
            else:
                if self.words[pointer-1][:length]==prefix:
                    idx=pointer
                right=pointer-1
        #print(f'bsL, idx: {idx}, points to {self.words[idx%len(self.words)]}')
        return idx


a=Autocomplete('words_alpha.txt')