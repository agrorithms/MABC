from typing import Optional, Union, Tuple
from node import Node

class BinaryTree:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def add(self,toAdd: Union[Node,int]) -> None:
        if not isinstance(toAdd,Node):
            toAdd = Node(toAdd)
        if not self.head:
            self.head = toAdd
        else:
            self.head.add(toAdd)

        
           
    def min(self, start: Optional[int] = None) -> Optional[Node]:
        if not self.head:
            print('tree has no head')
            return
         
        if start:
            start=self._findNode(start)[1] # right now findnode finds both target and parent of target node
            if start:
                return start.min()
            else:
                print('start node does not exist')
                return
        else:
            return self.head.min()
        
    
    def max(self,start: Optional[Node] = None) -> Node:
        if not self.head:
            print('tree has no head')
            return
         
        if start:
            start=self._findNode(start)[1] # right now findnode finds both target and parent of target node
            if start:
                return start.max()
            else:
                print('start node does not exist')
                return
        else:
            return self.head.max()

    
    def contains(self, value: int) -> bool:
        return bool(self._findNode(value))
    
    def remove(self, value: int) -> None:
        if not self.head:
            print("tree has no head")
            return None
        
        parent, target = self._findNode(value)
        if target==self.head:
            self.head=None
        elif target:
            target.remove(value) #for now node's remove method requires a value param
        else:
            print('target value does not exist in {self}')
        

    def maxDepth(self):
        if not self.head:
            print("tree has no head")
            return None
        return self.head.maxDepth()
            
    def _findNode(self,value: int) -> Optional[Tuple[Optional['Node'], 'Node']]:
        if not self.head:
            return None
        
        prev: Optional[Node] = None
        curr: Node = self.head
        while curr:
            if value > curr.value:
                prev=curr
                curr = curr.right
            elif value < curr.value:
                prev=curr
                curr = curr.left
            else:
                return prev , curr
        return None
    

    def __repr__(self):
        return dict(head=self.head).__repr__()