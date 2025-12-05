from typing import Optional, Union, Tuple

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def add(self, toAdd: Union[int, 'Node']) -> None:
        if isinstance(toAdd,int):
            toAdd = Node(toAdd)
        if toAdd.value<self.value:
            if self.left:
                self.left.add(toAdd)
            else:
                self.left = toAdd
        elif toAdd.value>self.value:
            if self.right:
                self.right.add(toAdd)
            else:
                self.right = toAdd
        else: 
            return
        
    def min(self) -> 'Node':
        if not self.left:
            return self
        return self.left.min()

    def max(self) -> 'Node':
        if not self.right:
            return self
        return self.right.max()
    
    def contains(self, value: int) -> bool:
        return bool(self._findNode(value))
    
    def remove(self, value: int) -> None:
        if value < self.value:
            if self.left:
                if self.left.value == value:
                    target = self.left
                    if target.isLeaf():
                        self.left = None
                        return
                    self._replaceNode(target)
                    
                    return
                else:
                    return self.left.remove(value)
            else:
                return None

        elif value > self.value:
            if self.right:
                if self.right.value == value:
                    target = self.right
                    if target.isLeaf():
                        self.right = None
                        return
                    self._replaceNode(target)
                    return
                    
                else:
                    return self.right.remove(value)
            else: 
                return None
        else:
            self._replaceNode(self)
    
    def maxDepth(self,depth=0) -> int:
        newdepth=depth
        if self.left:
            newdepth = max(newdepth,self.left.maxDepth(depth+1))
        
        if self.right:
            newdepth = max(newdepth, self.right.maxDepth(depth+1))

        return newdepth
        
    
    def isLeaf(self) -> bool:
        return self.right == None and self.left == None

    def _replaceNode(self,child: 'Node') -> None:
        if child.left:
            newVal=child.left.max().value # combine these
            child.remove(newVal) # combine these
            child.value=newVal
            return
        elif child.right:
            newVal=child.right.min().value
            child.remove(newVal)
            child.value=newVal
            return

    def _findNode(self, value: int) -> Optional['Node']:
        if self.value == value:
            return self
        elif value < self.value:
            if self.left:
                return self.left._findNode(value)
            else:
                return None
        elif value > self.value:
            if self.right:
                return self.right._findNode(value)
            else:
                return None

        
    def __bool__(self) -> bool:
        return self.value != None

    def __repr__(self) -> str:
        return dict(value = self.value, left=self.left.value if self.left else None,right=self.right.value if self.right else None).__repr__()
    
    def __eq__(self,other: object) -> bool:

        #recursive

        if not isinstance(other, Node):
            return False
        return self.value == other.value and self.left == other.left and self.right == other.right