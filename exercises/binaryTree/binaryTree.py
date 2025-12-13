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
            return None
         
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
        return bool(self._findNode(value)[1])
    
    def remove(self, value: int) -> None:
        if not self.head:
            print("tree has no head")
            return 
        
        parent, target = self._findNode(value)
        if not target:
            print('target value does not exist in {self}')
            return
        
        else:
            target.value = self._privRemove(target,parent)
            """
            delValue = target._remove().value
            print(f"{value=},{delValue=}")
            if delValue == self.head.value:
                print(f"{self.head=}, removing head")
                self.head=None
                return
            else:

                delParent = self._findNode(delValue)[0]
                
                if delValue>delParent.value:
                    delParent.right = None
                else:
                    delParent.left = None
                """

        
    def _privRemove(self, target: Node ,parent: Optional[Node]):
        headIsTarget=False
        if not parent:
            headIsTarget=True
        else:
            rightSide = parent.value<target.value
        if target.isLeaf():
            if headIsTarget:
                self.head=None
            elif rightSide:
                parent.right = None
            else:
                parent.left = None
            return target.value # return target.value to indicate target was removed and no further recursion
        if not target.left:
            if not parent:
                self.head = target.right
            elif rightSide:
                parent.right = target.right
            else:
                parent.left = target.right
            return target.value # return target.value to indicate target was removed and no further recursion
        elif not target.right:
            if not parent:
                self.head = target.left
            elif rightSide:
                parent.right = target.left
            else:
                parent.left = target.left
            return target.value # return target.value to indicate target was removed and no further recursion
        else:
            newParent,newTarget = target.left._maxRetParent()
            if not newParent:
                newParent = target
            return self._privRemove(newTarget,newParent)  # return in order predecessor
            
        
    
        return




    def maxDepth(self):
        if not self.head:
            print("tree has no head")
            return None
        return self.head.maxDepth()
            
    def _findNode(self,value: int) -> Tuple[Optional['Node'], Optional['Node']]:
        if not self.head:
            return None, None
        
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
        return None, None
    

    def __repr__(self):
        return dict(head=self.head).__repr__()