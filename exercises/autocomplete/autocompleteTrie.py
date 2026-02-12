import time
from functools import wraps
from typing import Union, Literal, Callable

def timeWrapper(func: Callable):
    def wrapper(*args,**kwargs):
        startTime: float =time.time()
        res = func(*args, **kwargs)
        elapsedTime: float = time.time()-startTime
        print(f'Results found in {elapsedTime*1000:.5f} milliseconds')
        return res
    return wrapper

class TrieNode():
    __slots__ = ('isEnd', 'children')
    def __init__(self) -> None:
        self.isEnd: bool = False
        self.children: dict[str,TrieNode] = {}


class Trie():
    def __init__(self) -> None:
        self.root : TrieNode = TrieNode()
    
    def insert(self,word: str) -> None:
        node: TrieNode = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True
    
    def searchPrefix(self, prefix: str) -> Union[TrieNode,Literal[False]]:
        node: TrieNode = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return node
            



class Autocomplete():
    def __init__(self,wordsFile: str) -> None:
        self.trie: Trie  = Trie()
        with open(wordsFile) as f:
            for line in f:
                self.trie.insert(line[:-1])
        self.prompt()
    
    def prompt(self) -> None:
        prefix: str = input('Enter a prefix: ').lower()
        if prefix.isalpha():
            if prefix in 'qx':
                if self.quit(): return
            self.print_results(prefix)
                    
        else:
            print('Prefix must contain alphabetical characters only.')
        
        self.prompt() 



    def quit(self) -> bool:
        quit: str = input('Would you like to quit? (Answer with "y" or "n"): ').lower()
        if quit:
            if quit == 'y':
                return True
            elif quit == 'n':
                return False
        
        print('Answer with y or n')
        return self.quit()
    
    @timeWrapper
    def print_results(self, prefix: str):
        startNode: Union[TrieNode,Literal[False]] = self.trie.searchPrefix(prefix)
        if not startNode:
            print('No results found.')
        else:
            numResults=self._get_results(startNode, prefix)
            if numResults>20:
                print(f'{numResults-20} more matches found')

    def _get_results(self,node: TrieNode, word: str, wordCount: int = 0) -> int:
        if node.isEnd:
            wordCount+=1
            if wordCount<=20:
                print(word)
            
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c in node.children:
                wordCount = self._get_results(node.children[c],word+c,wordCount)
        return wordCount
        
a=Autocomplete('words_alpha.txt')



        


    


    

